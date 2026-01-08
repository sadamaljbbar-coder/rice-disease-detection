/**
 * Rice Disease Detection System - Frontend Application
 * Handles image upload, API communication, and result display
 */

// ============================================================
// Configuration
// ============================================================
const CONFIG = {
    API_BASE_URL: window.location.origin + '/api',
    // Jika backend berjalan di port berbeda, gunakan:
    // API_BASE_URL: 'http://localhost:5000/api',
    MAX_FILE_SIZE: 10 * 1024 * 1024, // 10MB
    ALLOWED_TYPES: ['image/jpeg', 'image/png', 'image/webp', 'image/gif']
};

// ============================================================
// DOM Elements
// ============================================================
const elements = {
    // Upload
    uploadArea: document.getElementById('uploadArea'),
    uploadContent: document.getElementById('uploadContent'),
    previewContent: document.getElementById('previewContent'),
    loadingContent: document.getElementById('loadingContent'),
    imageInput: document.getElementById('imageInput'),
    selectBtn: document.getElementById('selectBtn'),
    cameraBtn: document.getElementById('cameraBtn'),
    previewImage: document.getElementById('previewImage'),
    analyzeBtn: document.getElementById('analyzeBtn'),
    resetBtn: document.getElementById('resetBtn'),
    
    // Results
    resultsArea: document.getElementById('resultsArea'),
    detectionCard: document.getElementById('detectionCard'),
    detectionResult: document.getElementById('detectionResult'),
    diseaseCard: document.getElementById('diseaseCard'),
    diseaseInfo: document.getElementById('diseaseInfo'),
    treatmentCard: document.getElementById('treatmentCard'),
    treatmentContent: document.getElementById('treatmentContent'),
    priorityCard: document.getElementById('priorityCard'),
    priorityContent: document.getElementById('priorityContent'),
    newAnalysisBtn: document.getElementById('newAnalysisBtn'),
    
    // Disease Database
    diseaseGrid: document.getElementById('diseaseGrid'),
    
    // Camera Modal
    cameraModal: document.getElementById('cameraModal'),
    cameraVideo: document.getElementById('cameraVideo'),
    cameraCanvas: document.getElementById('cameraCanvas'),
    captureBtn: document.getElementById('captureBtn'),
    cancelCameraBtn: document.getElementById('cancelCameraBtn'),
    closeCameraModal: document.getElementById('closeCameraModal'),
    
    // Disease Modal
    diseaseModal: document.getElementById('diseaseModal'),
    diseaseModalTitle: document.getElementById('diseaseModalTitle'),
    diseaseModalBody: document.getElementById('diseaseModalBody'),
    closeDiseaseModal: document.getElementById('closeDiseaseModal'),
    
    // Toast
    toast: document.getElementById('toast')
};

// ============================================================
// State
// ============================================================
let currentImageFile = null;
let currentImageBase64 = null;
let cameraStream = null;
let currentRecommendation = null;

// ============================================================
// Utility Functions
// ============================================================

/**
 * Show toast notification
 */
function showToast(message, type = 'info') {
    const toast = elements.toast;
    const toastMessage = toast.querySelector('.toast-message');
    const toastIcon = toast.querySelector('.toast-icon');
    
    // Set icon based on type
    const icons = {
        success: 'fas fa-check-circle',
        error: 'fas fa-exclamation-circle',
        warning: 'fas fa-exclamation-triangle',
        info: 'fas fa-info-circle'
    };
    
    toastIcon.className = `toast-icon ${icons[type] || icons.info}`;
    toastMessage.textContent = message;
    
    toast.className = `toast ${type}`;
    toast.classList.remove('hidden');
    
    // Auto hide after 4 seconds
    setTimeout(() => {
        toast.classList.add('hidden');
    }, 4000);
}

/**
 * Format confidence percentage
 */
function formatConfidence(confidence) {
    if (confidence > 1) return confidence.toFixed(1) + '%';
    return (confidence * 100).toFixed(1) + '%';
}

/**
 * Get severity color class
 */
function getSeverityClass(severity) {
    const classes = {
        'very_high': 'severity-very_high',
        'critical': 'severity-critical',
        'high': 'severity-high',
        'medium': 'severity-medium',
        'low': 'severity-low',
        'none': 'severity-none'
    };
    return classes[severity] || 'severity-medium';
}

/**
 * Convert file to base64
 */
function fileToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(file);
    });
}

/**
 * Validate image file
 */
function validateImage(file) {
    if (!file) {
        return { valid: false, error: 'Tidak ada file yang dipilih' };
    }
    
    if (!CONFIG.ALLOWED_TYPES.includes(file.type)) {
        return { valid: false, error: 'Format file tidak didukung. Gunakan JPG, PNG, atau WebP' };
    }
    
    if (file.size > CONFIG.MAX_FILE_SIZE) {
        return { valid: false, error: 'Ukuran file terlalu besar. Maksimal 10MB' };
    }
    
    return { valid: true };
}

// ============================================================
// UI Functions
// ============================================================

/**
 * Show upload state
 */
function showUploadState() {
    elements.uploadContent.classList.remove('hidden');
    elements.previewContent.classList.add('hidden');
    elements.loadingContent.classList.add('hidden');
    elements.resultsArea.classList.add('hidden');
}

/**
 * Show preview state
 */
function showPreviewState() {
    elements.uploadContent.classList.add('hidden');
    elements.previewContent.classList.remove('hidden');
    elements.loadingContent.classList.add('hidden');
    elements.resultsArea.classList.add('hidden');
}

/**
 * Show loading state
 */
function showLoadingState() {
    elements.uploadContent.classList.add('hidden');
    elements.previewContent.classList.add('hidden');
    elements.loadingContent.classList.remove('hidden');
    elements.resultsArea.classList.add('hidden');
}

/**
 * Show results state
 */
function showResultsState() {
    elements.uploadContent.classList.add('hidden');
    elements.previewContent.classList.add('hidden');
    elements.loadingContent.classList.add('hidden');
    elements.resultsArea.classList.remove('hidden');
}

/**
 * Reset to initial state
 */
function resetState() {
    currentImageFile = null;
    currentImageBase64 = null;
    currentRecommendation = null;
    elements.previewImage.src = '';
    elements.imageInput.value = '';
    showUploadState();
}

// ============================================================
// Image Handling
// ============================================================

/**
 * Handle image selection
 */
async function handleImageSelect(file) {
    const validation = validateImage(file);
    
    if (!validation.valid) {
        showToast(validation.error, 'error');
        return;
    }
    
    currentImageFile = file;
    
    try {
        currentImageBase64 = await fileToBase64(file);
        elements.previewImage.src = currentImageBase64;
        showPreviewState();
        showToast('Gambar berhasil dimuat', 'success');
    } catch (error) {
        showToast('Gagal memuat gambar', 'error');
        console.error('Error loading image:', error);
    }
}

/**
 * Handle drag and drop
 */
function setupDragDrop() {
    const uploadArea = elements.uploadArea;
    
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
        });
    });
    
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.classList.add('dragover');
        });
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.classList.remove('dragover');
        });
    });
    
    uploadArea.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleImageSelect(files[0]);
        }
    });
}

// ============================================================
// Camera Functions
// ============================================================

/**
 * Open camera modal
 */
async function openCamera() {
    try {
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: 'environment' }
        });
        
        elements.cameraVideo.srcObject = cameraStream;
        elements.cameraModal.classList.remove('hidden');
    } catch (error) {
        showToast('Tidak dapat mengakses kamera', 'error');
        console.error('Camera error:', error);
    }
}

/**
 * Close camera modal
 */
function closeCamera() {
    if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
    }
    elements.cameraModal.classList.add('hidden');
}

/**
 * Capture photo from camera
 */
function capturePhoto() {
    const video = elements.cameraVideo;
    const canvas = elements.cameraCanvas;
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);
    
    canvas.toBlob((blob) => {
        const file = new File([blob], 'camera-capture.jpg', { type: 'image/jpeg' });
        handleImageSelect(file);
        closeCamera();
    }, 'image/jpeg', 0.9);
}

// ============================================================
// API Functions
// ============================================================

/**
 * Send image for detection
 */
async function detectDisease() {
    if (!currentImageBase64) {
        showToast('Pilih gambar terlebih dahulu', 'warning');
        return;
    }
    
    showLoadingState();
    
    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/detect`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image_base64: currentImageBase64
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            currentRecommendation = result.data.recommendation;
            displayResults(result.data);
            showResultsState();
            showToast('Analisis selesai!', 'success');
        } else {
            throw new Error(result.error || 'Gagal melakukan deteksi');
        }
    } catch (error) {
        console.error('Detection error:', error);
        showToast(error.message || 'Terjadi kesalahan saat analisis', 'error');
        showPreviewState();
    }
}

/**
 * Fetch disease list
 */
async function fetchDiseases() {
    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/diseases`);
        const result = await response.json();
        
        if (result.success) {
            displayDiseaseGrid(result.data.diseases);
        }
    } catch (error) {
        console.error('Error fetching diseases:', error);
    }
}

/**
 * Fetch disease details
 */
async function fetchDiseaseDetails(diseaseKey) {
    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/diseases/${diseaseKey}`);
        const result = await response.json();
        
        if (result.success) {
            showDiseaseModal(result.data.disease);
        }
    } catch (error) {
        console.error('Error fetching disease details:', error);
        showToast('Gagal memuat detail penyakit', 'error');
    }
}

// ============================================================
// Display Functions
// ============================================================

/**
 * Display detection results
 */
function displayResults(data) {
    const { detection, recommendation } = data;
    
    // Display detection result
    displayDetectionResult(detection, recommendation);
    
    // Display disease info
    displayDiseaseInfo(recommendation);
    
    // Display treatments
    displayTreatments(recommendation.treatments);
    
    // Display priority
    displayPriority(recommendation.action_priority);
}

/**
 * Display detection result
 */
function displayDetectionResult(detection, recommendation) {
    const diseaseInfo = recommendation.disease_info;
    const confidence = detection.confidence;
    
    let html = `
        <div class="disease-name">${diseaseInfo.name_id}</div>
        <div class="pathogen-name">${diseaseInfo.pathogen || 'Tidak ada patogen'}</div>
        <div class="confidence-bar">
            <div class="confidence-fill" style="width: ${confidence}%">${confidence}%</div>
        </div>
        <div class="confidence-label">Tingkat Kepercayaan Model</div>
        <div style="margin-top: 1rem;">
            <span class="severity-badge ${getSeverityClass(diseaseInfo.severity)}">
                Tingkat Keparahan: ${diseaseInfo.severity === 'none' ? 'Tidak Ada' : diseaseInfo.severity.toUpperCase()}
            </span>
        </div>
        <div style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.9rem;">
            Potensi Kehilangan Hasil: ${diseaseInfo.potential_yield_loss}
        </div>
    `;
    
    elements.detectionResult.innerHTML = html;
}

/**
 * Display disease information
 */
function displayDiseaseInfo(recommendation) {
    const { symptoms, favorable_conditions } = recommendation;
    
    let html = '';
    
    if (symptoms && symptoms.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-stethoscope"></i> Gejala</h4>
                <ul>
                    ${symptoms.map(s => `<li>${s}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    if (favorable_conditions && favorable_conditions.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-cloud-sun"></i> Kondisi yang Mendukung</h4>
                <ul>
                    ${favorable_conditions.map(c => `<li>${c}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    if (recommendation.prevention && recommendation.prevention.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-shield-alt"></i> Pencegahan</h4>
                <ul>
                    ${recommendation.prevention.map(p => `<li>${p}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    // For healthy leaves
    if (recommendation.maintenance_tips && recommendation.maintenance_tips.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-lightbulb"></i> Tips Pemeliharaan</h4>
                <ul>
                    ${recommendation.maintenance_tips.map(t => `<li>${t}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    elements.diseaseInfo.innerHTML = html || '<p class="text-muted">Tidak ada informasi tambahan</p>';
}

/**
 * Display treatments with tabs
 */
function displayTreatments(treatments) {
    if (!treatments) {
        elements.treatmentContent.innerHTML = '<p class="text-muted">Tidak ada rekomendasi treatment</p>';
        return;
    }
    
    // Store treatments for tab switching
    window.currentTreatments = treatments;
    
    // Show chemical tab by default
    showTreatmentTab('chemical');
    
    // Setup tab click handlers
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            showTreatmentTab(btn.dataset.tab);
        });
    });
}

/**
 * Show specific treatment tab
 */
function showTreatmentTab(tabName) {
    const treatments = window.currentTreatments;
    if (!treatments) return;
    
    const treatment = treatments[tabName];
    if (!treatment) {
        elements.treatmentContent.innerHTML = '<p class="text-muted">Tidak ada data</p>';
        return;
    }
    
    let html = '';
    
    if (tabName === 'cultural') {
        // Cultural practices as list
        if (treatment.options && treatment.options.length > 0) {
            html = `
                <ul class="cultural-list">
                    ${treatment.options.map(opt => `
                        <li><i class="fas fa-check"></i> ${opt}</li>
                    `).join('')}
                </ul>
            `;
        } else {
            html = '<p class="text-muted">Tidak ada rekomendasi kultur teknis</p>';
        }
    } else {
        // Chemical or biological treatments
        if (treatment.options && treatment.options.length > 0) {
            html = `
                <div class="treatment-list">
                    ${treatment.options.map(opt => `
                        <div class="treatment-item">
                            <h4>${opt.name}</h4>
                            ${opt.brand_examples ? `
                                <p class="brand-examples">
                                    <i class="fas fa-tag"></i> Contoh merek: ${opt.brand_examples.join(', ')}
                                </p>
                            ` : ''}
                            ${opt.dosage ? `<p><i class="fas fa-prescription"></i> Dosis: ${opt.dosage}</p>` : ''}
                            ${opt.application ? `<p><i class="fas fa-spray-can"></i> Aplikasi: ${opt.application}</p>` : ''}
                            ${opt.interval ? `<p><i class="fas fa-clock"></i> Interval: ${opt.interval}</p>` : ''}
                            ${opt.notes ? `<p><i class="fas fa-info-circle"></i> ${opt.notes}</p>` : ''}
                        </div>
                    `).join('')}
                </div>
            `;
        } else {
            html = `<p class="text-muted">Tidak ada rekomendasi ${tabName === 'chemical' ? 'kimiawi' : 'hayati'}</p>`;
        }
    }
    
    elements.treatmentContent.innerHTML = html;
}

/**
 * Display action priority
 */
function displayPriority(priority) {
    if (!priority) {
        elements.priorityContent.innerHTML = '';
        return;
    }
    
    const levelColors = {
        critical: 'var(--danger)',
        high: 'var(--warning)',
        medium: 'var(--info)',
        low: 'var(--success)'
    };
    
    const levelLabels = {
        critical: 'KRITIS - Segera Bertindak!',
        high: 'TINGGI - Tindakan Segera',
        medium: 'SEDANG - Perlu Perhatian',
        low: 'RENDAH - Pemantauan Rutin'
    };
    
    elements.priorityContent.innerHTML = `
        <div class="priority-level" style="color: ${levelColors[priority.level] || 'var(--text-primary)'}">
            <i class="fas fa-exclamation-circle"></i> ${levelLabels[priority.level] || priority.level.toUpperCase()}
        </div>
        <p class="priority-message">${priority.message}</p>
    `;
}

/**
 * Display disease grid
 */
function displayDiseaseGrid(diseases) {
    if (!diseases || diseases.length === 0) {
        elements.diseaseGrid.innerHTML = '<p class="text-muted">Tidak ada data penyakit</p>';
        return;
    }
    
    const html = diseases.map(disease => `
        <div class="disease-card" data-disease="${disease.key}">
            <div class="disease-card-header">
                <div>
                    <h3>${disease.name_id}</h3>
                    <p class="pathogen">${disease.name_en}</p>
                </div>
                <span class="severity-badge ${getSeverityClass(disease.severity)}">
                    ${disease.severity === 'none' ? 'Sehat' : disease.severity}
                </span>
            </div>
            <div class="view-more">
                <span>Lihat Detail</span>
                <i class="fas fa-arrow-right"></i>
            </div>
        </div>
    `).join('');
    
    elements.diseaseGrid.innerHTML = html;
    
    // Add click handlers
    document.querySelectorAll('.disease-card').forEach(card => {
        card.addEventListener('click', () => {
            fetchDiseaseDetails(card.dataset.disease);
        });
    });
}

/**
 * Show disease modal
 */
function showDiseaseModal(disease) {
    elements.diseaseModalTitle.textContent = disease.name;
    
    let html = `
        <div class="disease-info">
            <p><strong>Patogen:</strong> <em>${disease.pathogen || '-'}</em></p>
            <p><strong>Potensi Kehilangan Hasil:</strong> ${disease.yield_loss}</p>
            
            <div class="info-section">
                <h4><i class="fas fa-stethoscope"></i> Gejala</h4>
                <ul>
                    ${disease.symptoms.map(s => `<li>${s}</li>`).join('')}
                </ul>
            </div>
    `;
    
    if (disease.favorable_conditions && disease.favorable_conditions.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-cloud-sun"></i> Kondisi yang Mendukung</h4>
                <ul>
                    ${disease.favorable_conditions.map(c => `<li>${c}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    if (disease.treatments && disease.treatments.chemical && disease.treatments.chemical.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-flask"></i> Pengendalian Kimiawi</h4>
                <ul>
                    ${disease.treatments.chemical.map(t => `<li><strong>${t.name}</strong> - ${t.dosage || ''}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    if (disease.prevention && disease.prevention.length > 0) {
        html += `
            <div class="info-section">
                <h4><i class="fas fa-shield-alt"></i> Pencegahan</h4>
                <ul>
                    ${disease.prevention.map(p => `<li>${p}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    html += '</div>';
    
    elements.diseaseModalBody.innerHTML = html;
    elements.diseaseModal.classList.remove('hidden');
}

/**
 * Close disease modal
 */
function closeDiseaseModal() {
    elements.diseaseModal.classList.add('hidden');
}

// ============================================================
// Event Listeners
// ============================================================

function setupEventListeners() {
    // File input
    elements.imageInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleImageSelect(e.target.files[0]);
        }
    });
    
    // Select button
    elements.selectBtn.addEventListener('click', () => {
        elements.imageInput.click();
    });
    
    // Camera button
    elements.cameraBtn.addEventListener('click', openCamera);
    
    // Analyze button
    elements.analyzeBtn.addEventListener('click', detectDisease);
    
    // Reset button
    elements.resetBtn.addEventListener('click', resetState);
    
    // New analysis button
    elements.newAnalysisBtn.addEventListener('click', resetState);
    
    // Camera modal
    elements.captureBtn.addEventListener('click', capturePhoto);
    elements.cancelCameraBtn.addEventListener('click', closeCamera);
    elements.closeCameraModal.addEventListener('click', closeCamera);
    
    // Disease modal
    elements.closeDiseaseModal.addEventListener('click', closeDiseaseModal);
    
    // Close modals on backdrop click
    elements.cameraModal.addEventListener('click', (e) => {
        if (e.target === elements.cameraModal) closeCamera();
    });
    
    elements.diseaseModal.addEventListener('click', (e) => {
        if (e.target === elements.diseaseModal) closeDiseaseModal();
    });
    
    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeCamera();
            closeDiseaseModal();
        }
    });
    
    // Smooth scroll for nav links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
            
            // Update active state
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });
}

// ============================================================
// Initialization
// ============================================================

function init() {
    console.log('🌾 Rice Disease Detection System initialized');
    
    // Setup drag and drop
    setupDragDrop();
    
    // Setup event listeners
    setupEventListeners();
    
    // Fetch disease list
    fetchDiseases();
    
    // Check API health
    fetch(`${CONFIG.API_BASE_URL}/health`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                console.log('✅ API is healthy:', data.data);
            }
        })
        .catch(err => {
            console.warn('⚠️ API health check failed:', err);
            showToast('Backend API tidak tersedia. Pastikan server berjalan.', 'warning');
        });
}

// Start the application
document.addEventListener('DOMContentLoaded', init);
