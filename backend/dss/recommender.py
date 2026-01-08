"""
Treatment Recommender Engine
Generates recommendations based on disease classification results
"""
from .knowledge_base import DiseaseKnowledgeBase


class TreatmentRecommender:
    """
    Decision Support System for generating treatment recommendations
    """
    
    def __init__(self):
        self.knowledge_base = DiseaseKnowledgeBase
        
    def get_recommendation(self, disease_class, confidence=0.0):
        """
        Generate comprehensive treatment recommendation
        
        Args:
            disease_class: Detected disease class
            confidence: Confidence score from model (0-1)
            
        Returns:
            dict: Complete recommendation with disease info and treatments
        """
        # Get disease information
        disease_info = self.knowledge_base.get_disease_info(disease_class)
        
        if not disease_info:
            return {
                'success': False,
                'error': f'Disease class "{disease_class}" not found in knowledge base',
                'suggestion': 'Please check the disease class name'
            }
        
        # Build recommendation
        recommendation = {
            'success': True,
            'detection': {
                'disease_class': disease_class,
                'confidence': round(confidence * 100, 2),
                'confidence_level': self._get_confidence_level(confidence)
            },
            'disease_info': {
                'name': disease_info['name'],
                'name_id': disease_info['name_id'],
                'name_en': disease_info['name_en'],
                'pathogen': disease_info['pathogen'],
                'pathogen_type': disease_info['pathogen_type'],
                'severity': disease_info['severity'],
                'potential_yield_loss': disease_info['yield_loss']
            },
            'symptoms': disease_info['symptoms'],
            'favorable_conditions': disease_info['favorable_conditions'],
            'treatments': self._format_treatments(disease_info['treatments']),
            'prevention': disease_info['prevention'],
            'general_tips': self.knowledge_base.get_general_info(),
            'action_priority': self._get_action_priority(disease_class, confidence)
        }
        
        # Add maintenance tips for healthy leaves
        if disease_class == 'healthy':
            recommendation['maintenance_tips'] = disease_info.get('maintenance_tips', [])
        
        return recommendation
    
    def _get_confidence_level(self, confidence):
        """Determine confidence level category"""
        if confidence >= 0.9:
            return 'very_high'
        elif confidence >= 0.75:
            return 'high'
        elif confidence >= 0.5:
            return 'medium'
        else:
            return 'low'
    
    def _get_action_priority(self, disease_class, confidence):
        """Determine action priority based on disease and confidence"""
        if disease_class == 'healthy':
            return {
                'level': 'low',
                'message': 'Tidak diperlukan tindakan khusus. Lakukan pemantauan rutin.',
                'urgency': 'routine_monitoring'
            }
        
        severity_priority = {
            'very_high': 'critical',
            'high': 'high',
            'medium': 'medium',
            'low': 'low'
        }
        
        disease_info = self.knowledge_base.get_disease_info(disease_class)
        severity = disease_info.get('severity', 'medium') if disease_info else 'medium'
        
        if confidence >= 0.8:
            if severity in ['very_high', 'high']:
                return {
                    'level': 'critical',
                    'message': 'Segera lakukan tindakan pengendalian! Penyakit terdeteksi dengan tingkat kepercayaan tinggi.',
                    'urgency': 'immediate_action'
                }
            else:
                return {
                    'level': 'high',
                    'message': 'Lakukan tindakan pengendalian dalam 1-2 hari.',
                    'urgency': 'urgent'
                }
        elif confidence >= 0.5:
            return {
                'level': 'medium',
                'message': 'Perlu verifikasi lebih lanjut. Siapkan tindakan pengendalian.',
                'urgency': 'verify_and_prepare'
            }
        else:
            return {
                'level': 'low',
                'message': 'Tingkat kepercayaan rendah. Lakukan pemeriksaan ulang dengan foto yang lebih jelas.',
                'urgency': 'recheck'
            }
    
    def _format_treatments(self, treatments):
        """Format treatments for presentation"""
        formatted = {
            'chemical': {
                'title': 'Pengendalian Kimiawi (Pestisida)',
                'description': 'Gunakan pestisida sebagai opsi ketika serangan sudah cukup parah',
                'options': treatments.get('chemical', []),
                'priority': 'secondary'
            },
            'biological': {
                'title': 'Pengendalian Hayati (Biokontrol)',
                'description': 'Metode ramah lingkungan menggunakan mikroorganisme antagonis',
                'options': treatments.get('biological', []),
                'priority': 'recommended'
            },
            'cultural': {
                'title': 'Pengendalian Kultur Teknis',
                'description': 'Praktik budidaya untuk mencegah dan mengurangi serangan',
                'options': treatments.get('cultural', []),
                'priority': 'primary'
            }
        }
        
        return formatted
    
    def get_quick_recommendation(self, disease_class):
        """
        Get simplified quick recommendation
        
        Args:
            disease_class: Detected disease class
            
        Returns:
            dict: Simplified recommendation
        """
        disease_info = self.knowledge_base.get_disease_info(disease_class)
        
        if not disease_info:
            return None
        
        # Get primary chemical treatment
        chemical_treatments = disease_info['treatments'].get('chemical', [])
        primary_chemical = chemical_treatments[0] if chemical_treatments else None
        
        return {
            'disease': disease_info['name_id'],
            'pathogen': disease_info['pathogen'],
            'severity': disease_info['severity'],
            'primary_treatment': primary_chemical,
            'cultural_practices': disease_info['treatments'].get('cultural', [])[:3]
        }
    
    def compare_recommendations(self, disease_classes):
        """
        Compare recommendations for multiple possible diseases
        
        Args:
            disease_classes: List of (disease_class, confidence) tuples
            
        Returns:
            list: Sorted recommendations by confidence
        """
        recommendations = []
        
        for disease_class, confidence in disease_classes:
            rec = self.get_recommendation(disease_class, confidence)
            if rec.get('success'):
                recommendations.append(rec)
        
        # Sort by confidence descending
        recommendations.sort(key=lambda x: x['detection']['confidence'], reverse=True)
        
        return recommendations


# Convenience function for direct use
def get_treatment_recommendation(disease_class, confidence=0.0):
    """
    Quick function to get treatment recommendation
    
    Args:
        disease_class: Disease class from model
        confidence: Confidence score
        
    Returns:
        dict: Treatment recommendation
    """
    recommender = TreatmentRecommender()
    return recommender.get_recommendation(disease_class, confidence)
