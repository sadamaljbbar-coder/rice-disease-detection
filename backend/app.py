"""
Rice Disease Detection System - Main Flask Application
Web IoT Backend with Vision Transformer Integration and DSS
"""
import os
import sys
import json
import base64
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from roboflow_client import RoboflowClient
from dss.recommender import TreatmentRecommender
from dss.knowledge_base import DiseaseKnowledgeBase

# Initialize Flask app
app = Flask(__name__, static_folder='../frontend', static_url_path='')
app.config.from_object(Config)

# Enable CORS for all routes
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Initialize clients
roboflow_client = RoboflowClient()
recommender = TreatmentRecommender()


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def validate_image(file):
    """Validate uploaded image file"""
    if not file:
        return False, "No file provided"
    
    if file.filename == '':
        return False, "No file selected"
    
    if not Config.allowed_file(file.filename):
        return False, f"File type not allowed. Allowed: {', '.join(Config.ALLOWED_EXTENSIONS)}"
    
    return True, "Valid"


def format_response(success, data=None, error=None, status_code=200):
    """Format API response"""
    response = {
        'success': success,
        'timestamp': datetime.utcnow().isoformat(),
    }
    
    if data:
        response['data'] = data
    if error:
        response['error'] = error
        
    return jsonify(response), status_code


# ============================================================
# ROUTES - STATIC FILES
# ============================================================

@app.route('/')
def serve_frontend():
    """Serve the main frontend page"""
    return send_from_directory('../frontend', 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('../frontend', path)


# ============================================================
# ROUTES - API ENDPOINTS
# ============================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return format_response(True, {
        'status': 'healthy',
        'service': 'Rice Disease Detection API',
        'version': '1.0.0'
    })


@app.route('/api/detect', methods=['POST'])
def detect_disease():
    """
    Main detection endpoint
    Accepts image and returns disease classification with treatment recommendations
    
    Request:
        - Form data with 'image' file
        OR
        - JSON with 'image_base64' string
        OR
        - JSON with 'image_url' string
        
    Response:
        - Detection results with recommendations
    """
    try:
        result = None
        
        # Check for file upload
        if 'image' in request.files:
            file = request.files['image']
            valid, message = validate_image(file)
            
            if not valid:
                return format_response(False, error=message, status_code=400)
            
            # Read image bytes
            image_bytes = file.read()
            result = roboflow_client.classify(image_bytes=image_bytes)
            
        # Check for base64 image
        elif request.is_json and 'image_base64' in request.json:
            image_data = request.json['image_base64']
            # Remove data URL prefix if present
            if ',' in image_data:
                image_data = image_data.split(',')[1]
            
            image_bytes = base64.b64decode(image_data)
            result = roboflow_client.classify(image_bytes=image_bytes)
            
        # Check for image URL
        elif request.is_json and 'image_url' in request.json:
            image_url = request.json['image_url']
            result = roboflow_client.classify_url(image_url)
            
        else:
            return format_response(
                False, 
                error="No image provided. Send 'image' file, 'image_base64', or 'image_url'",
                status_code=400
            )
        
        # Check Roboflow result
        if not result.get('success'):
            return format_response(
                False,
                error=result.get('error', 'Classification failed'),
                status_code=500
            )
        
        # Get detected disease class
        # Handle different response formats from Roboflow
        predictions = result.get('predictions', {})
        
        if isinstance(predictions, dict):
            # Format: {'class_name': confidence, ...}
            if predictions:
                top_class = max(predictions.items(), key=lambda x: x[1])
                disease_class = top_class[0]
                confidence = top_class[1]
            else:
                disease_class = result.get('top_prediction', result.get('top', 'unknown'))
                confidence = result.get('confidence', 0)
        elif isinstance(predictions, list):
            # Format: [{'class': 'name', 'confidence': 0.9}, ...]
            if predictions:
                top_pred = max(predictions, key=lambda x: x.get('confidence', 0))
                disease_class = top_pred.get('class', 'unknown')
                confidence = top_pred.get('confidence', 0)
            else:
                disease_class = 'unknown'
                confidence = 0
        else:
            disease_class = result.get('top_prediction', result.get('top', 'unknown'))
            confidence = result.get('confidence', 0)
        
        # Get treatment recommendation
        recommendation = recommender.get_recommendation(disease_class, confidence)
        
        # Build response
        response_data = {
            'detection': {
                'disease_class': disease_class,
                'confidence': round(confidence * 100, 2) if confidence <= 1 else round(confidence, 2),
                'all_predictions': predictions
            },
            'recommendation': recommendation,
            'inference_time': result.get('time', 0)
        }
        
        return format_response(True, response_data)
        
    except Exception as e:
        app.logger.error(f"Detection error: {str(e)}")
        return format_response(False, error=str(e), status_code=500)


@app.route('/api/diseases', methods=['GET'])
def get_diseases():
    """Get list of all supported diseases"""
    diseases = []
    
    for key in DiseaseKnowledgeBase.get_all_diseases():
        info = DiseaseKnowledgeBase.get_disease_info(key)
        if info:
            diseases.append({
                'key': key,
                'name': info['name'],
                'name_id': info['name_id'],
                'name_en': info['name_en'],
                'severity': info['severity']
            })
    
    return format_response(True, {'diseases': diseases})


@app.route('/api/diseases/<disease_class>', methods=['GET'])
def get_disease_info(disease_class):
    """Get detailed information about a specific disease"""
    info = DiseaseKnowledgeBase.get_disease_info(disease_class)
    
    if not info:
        return format_response(
            False, 
            error=f"Disease '{disease_class}' not found",
            status_code=404
        )
    
    return format_response(True, {'disease': info})


@app.route('/api/treatments/<disease_class>', methods=['GET'])
def get_treatments(disease_class):
    """Get treatment recommendations for a specific disease"""
    treatment_type = request.args.get('type', 'all')
    
    treatments = DiseaseKnowledgeBase.get_treatments(disease_class, treatment_type)
    
    if treatments is None:
        return format_response(
            False,
            error=f"Disease '{disease_class}' not found",
            status_code=404
        )
    
    return format_response(True, {'treatments': treatments})


@app.route('/api/recommendation/<disease_class>', methods=['GET'])
def get_recommendation(disease_class):
    """Get full recommendation for a disease"""
    confidence = float(request.args.get('confidence', 0.95))
    
    recommendation = recommender.get_recommendation(disease_class, confidence)
    
    if not recommendation.get('success'):
        return format_response(
            False,
            error=recommendation.get('error'),
            status_code=404
        )
    
    return format_response(True, {'recommendation': recommendation})


@app.route('/api/general-info', methods=['GET'])
def get_general_info():
    """Get general application and safety information"""
    info = DiseaseKnowledgeBase.get_general_info()
    return format_response(True, {'info': info})


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def not_found(error):
    return format_response(False, error="Endpoint not found", status_code=404)


@app.errorhandler(413)
def file_too_large(error):
    return format_response(
        False, 
        error=f"File too large. Maximum size: {Config.MAX_CONTENT_LENGTH // (1024*1024)}MB",
        status_code=413
    )


@app.errorhandler(500)
def internal_error(error):
    return format_response(False, error="Internal server error", status_code=500)


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    print("=" * 60)
    print("🌾 Rice Disease Detection System")
    print("=" * 60)
    print(f"📡 Starting server on http://{Config.HOST}:{Config.PORT}")
    print(f"🔧 Debug mode: {Config.DEBUG}")
    print(f"🤖 Roboflow Model: {Config.ROBOFLOW_MODEL_ID}")
    print("=" * 60)
    
    # Check API key
    if not Config.ROBOFLOW_API_KEY:
        print("⚠️  WARNING: ROBOFLOW_API_KEY not set!")
        print("   Please set it in .env file")
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
