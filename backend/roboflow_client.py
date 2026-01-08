"""
Roboflow API Client for Rice Disease Detection
Handles communication with Roboflow Hosted Inference API
"""
import requests
import base64
import json
from config import Config


class RoboflowClient:
    """Client for Roboflow Vision Transformer Model"""
    
    def __init__(self):
        self.api_key = Config.ROBOFLOW_API_KEY
        self.model_id = Config.ROBOFLOW_MODEL_ID
        self.api_url = Config.ROBOFLOW_API_URL
        
    def _encode_image(self, image_path=None, image_bytes=None):
        """Encode image to base64"""
        if image_bytes:
            return base64.b64encode(image_bytes).decode('utf-8')
        elif image_path:
            with open(image_path, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        return None
    
    def classify(self, image_path=None, image_bytes=None):
        """
        Classify rice leaf disease using Roboflow ViT model
        
        Args:
            image_path: Path to image file
            image_bytes: Raw image bytes
            
        Returns:
            dict: Classification result with predictions
        """
        try:
            # Encode image to base64
            image_data = self._encode_image(image_path, image_bytes)
            
            if not image_data:
                return {
                    'success': False,
                    'error': 'No image data provided'
                }
            
            # Build API URL
            # For classification model, use classify endpoint
            url = f"https://classify.roboflow.com/{self.model_id}"
            
            # Make API request
            response = requests.post(
                url,
                params={
                    'api_key': self.api_key
                },
                data=image_data,
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                timeout=30
            )
            
            # Check response
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'predictions': result.get('predictions', []),
                    'top_prediction': result.get('top', ''),
                    'confidence': result.get('confidence', 0),
                    'time': result.get('time', 0)
                }
            else:
                return {
                    'success': False,
                    'error': f'API Error: {response.status_code}',
                    'message': response.text
                }
                
        except requests.exceptions.Timeout:
            return {
                'success': False,
                'error': 'Request timeout'
            }
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Request failed: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}'
            }
    
    def classify_url(self, image_url):
        """
        Classify rice leaf disease from image URL
        
        Args:
            image_url: URL of the image
            
        Returns:
            dict: Classification result
        """
        try:
            url = f"https://classify.roboflow.com/{self.model_id}"
            
            response = requests.post(
                url,
                params={
                    'api_key': self.api_key,
                    'image': image_url
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'predictions': result.get('predictions', []),
                    'top_prediction': result.get('top', ''),
                    'confidence': result.get('confidence', 0)
                }
            else:
                return {
                    'success': False,
                    'error': f'API Error: {response.status_code}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


# Alternative: Using Roboflow Inference SDK
class RoboflowSDKClient:
    """Alternative client using official Roboflow SDK"""
    
    def __init__(self):
        self.api_key = Config.ROBOFLOW_API_KEY
        self.model_id = Config.ROBOFLOW_MODEL_ID
        self._client = None
        
    def _get_client(self):
        """Lazy initialization of inference client"""
        if self._client is None:
            try:
                from inference_sdk import InferenceHTTPClient
                self._client = InferenceHTTPClient(
                    api_url="https://classify.roboflow.com",
                    api_key=self.api_key
                )
            except ImportError:
                raise ImportError("inference-sdk not installed. Run: pip install inference-sdk")
        return self._client
    
    def classify(self, image_path):
        """Classify using SDK"""
        try:
            client = self._get_client()
            result = client.infer(image_path, model_id=self.model_id)
            
            return {
                'success': True,
                'predictions': result.get('predictions', []),
                'top_prediction': result.get('top', ''),
                'confidence': result.get('confidence', 0)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
