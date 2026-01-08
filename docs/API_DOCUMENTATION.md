# 📚 API Documentation

## Rice Disease Detection System API

Base URL: `http://localhost:5000/api`

---

## Endpoints

### 1. Health Check

**GET** `/api/health`

Check if the API is running.

**Response:**
```json
{
    "success": true,
    "timestamp": "2026-01-08T10:30:00.000Z",
    "data": {
        "status": "healthy",
        "service": "Rice Disease Detection API",
        "version": "1.0.0"
    }
}
```

---

### 2. Detect Disease

**POST** `/api/detect`

Upload an image for disease detection and get treatment recommendations.

**Request Options:**

#### Option A: Form Data (File Upload)
```
Content-Type: multipart/form-data

image: [binary file]
```

#### Option B: JSON with Base64
```json
{
    "image_base64": "data:image/jpeg;base64,/9j/4AAQ..."
}
```

#### Option C: JSON with URL
```json
{
    "image_url": "https://example.com/image.jpg"
}
```

**Response:**
```json
{
    "success": true,
    "timestamp": "2026-01-08T10:30:00.000Z",
    "data": {
        "detection": {
            "disease_class": "leaf_blast",
            "confidence": 98.5,
            "all_predictions": {
                "leaf_blast": 0.985,
                "brown_spot": 0.008,
                "healthy": 0.005,
                "bacterial_leaf_blight": 0.002
            }
        },
        "recommendation": {
            "success": true,
            "detection": {
                "disease_class": "leaf_blast",
                "confidence": 98.5,
                "confidence_level": "very_high"
            },
            "disease_info": {
                "name": "Leaf Blast (Blas Daun)",
                "name_id": "Blas Daun",
                "name_en": "Rice Blast",
                "pathogen": "Pyricularia oryzae",
                "pathogen_type": "fungus",
                "severity": "very_high",
                "potential_yield_loss": "10-100%"
            },
            "symptoms": [...],
            "favorable_conditions": [...],
            "treatments": {
                "chemical": {...},
                "biological": {...},
                "cultural": {...}
            },
            "prevention": [...],
            "action_priority": {
                "level": "critical",
                "message": "Segera lakukan tindakan pengendalian!",
                "urgency": "immediate_action"
            }
        },
        "inference_time": 0.245
    }
}
```

---

### 3. Get All Diseases

**GET** `/api/diseases`

Get list of all supported diseases.

**Response:**
```json
{
    "success": true,
    "data": {
        "diseases": [
            {
                "key": "bacterial_leaf_blight",
                "name": "Bacterial Leaf Blight (Hawar Daun Bakteri)",
                "name_id": "Hawar Daun Bakteri",
                "name_en": "Bacterial Leaf Blight (BLB)",
                "severity": "high"
            },
            ...
        ]
    }
}
```

---

### 4. Get Disease Details

**GET** `/api/diseases/{disease_class}`

Get detailed information about a specific disease.

**Parameters:**
- `disease_class`: Disease identifier (e.g., `leaf_blast`, `brown_spot`)

**Response:**
```json
{
    "success": true,
    "data": {
        "disease": {
            "name": "Leaf Blast (Blas Daun)",
            "pathogen": "Pyricularia oryzae",
            "symptoms": [...],
            "treatments": {...},
            ...
        }
    }
}
```

---

### 5. Get Treatments

**GET** `/api/treatments/{disease_class}`

Get treatment recommendations for a specific disease.

**Parameters:**
- `disease_class`: Disease identifier
- `type` (optional): Filter by treatment type (`chemical`, `biological`, `cultural`, or `all`)

**Example:**
```
GET /api/treatments/leaf_blast?type=chemical
```

**Response:**
```json
{
    "success": true,
    "data": {
        "treatments": [
            {
                "name": "Tricyclazole",
                "brand_examples": ["Beam 75 WP", "Blas 75 WP"],
                "dosage": "1 g/L air",
                "application": "Semprot preventif atau saat gejala awal",
                "interval": "Setiap 10-14 hari",
                "notes": "Fungisida spesifik blast, sangat efektif"
            },
            ...
        ]
    }
}
```

---

### 6. Get Recommendation

**GET** `/api/recommendation/{disease_class}`

Get full treatment recommendation for a disease.

**Parameters:**
- `disease_class`: Disease identifier
- `confidence` (optional): Confidence score (0-1), default: 0.95

**Example:**
```
GET /api/recommendation/leaf_blast?confidence=0.98
```

---

### 7. Get General Info

**GET** `/api/general-info`

Get general application tips and safety information.

**Response:**
```json
{
    "success": true,
    "data": {
        "info": {
            "application_tips": [...],
            "safety_precautions": [...],
            "integrated_pest_management": [...]
        }
    }
}
```

---

## Error Responses

All endpoints return errors in this format:

```json
{
    "success": false,
    "timestamp": "2026-01-08T10:30:00.000Z",
    "error": "Error message describing what went wrong"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `404` - Not Found (disease not found)
- `413` - Payload Too Large (file > 16MB)
- `500` - Internal Server Error

---

## Disease Classes

The system supports the following disease classes:

| Key | Indonesian Name | English Name |
|-----|-----------------|--------------|
| `bacterial_leaf_blight` | Hawar Daun Bakteri | Bacterial Leaf Blight |
| `brown_spot` | Bercak Coklat | Brown Spot |
| `leaf_blast` | Blas Daun | Rice Blast |
| `leaf_scald` | Lepuh Daun | Leaf Scald |
| `narrow_brown_spot` | Bercak Coklat Sempit | Narrow Brown Leaf Spot |
| `healthy` | Daun Sehat | Healthy Leaf |

---

## Usage Examples

### Python
```python
import requests
import base64

# Read image
with open('leaf_image.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

# Send request
response = requests.post(
    'http://localhost:5000/api/detect',
    json={'image_base64': image_data}
)

result = response.json()
print(result['data']['recommendation']['disease_info']['name_id'])
```

### JavaScript
```javascript
// Using fetch with File
const formData = new FormData();
formData.append('image', fileInput.files[0]);

const response = await fetch('/api/detect', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log(result.data.recommendation.disease_info.name_id);
```

### cURL
```bash
# With file
curl -X POST -F "image=@leaf_image.jpg" http://localhost:5000/api/detect

# With URL
curl -X POST -H "Content-Type: application/json" \
  -d '{"image_url":"https://example.com/leaf.jpg"}' \
  http://localhost:5000/api/detect
```
