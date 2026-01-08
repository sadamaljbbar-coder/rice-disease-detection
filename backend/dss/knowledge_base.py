"""
Knowledge Base for Rice Disease Detection System
Contains comprehensive information about diseases and treatments
Based on IRRI Rice Knowledge Bank and Indonesian Agricultural Guidelines
"""


class DiseaseKnowledgeBase:
    """
    Knowledge base containing disease information and treatment recommendations
    """
    
    # Disease Information Database
    DISEASES = {
        'bacterial_leaf_blight': {
            'name': 'Bacterial Leaf Blight (Hawar Daun Bakteri)',
            'name_id': 'Hawar Daun Bakteri',
            'name_en': 'Bacterial Leaf Blight (BLB)',
            'pathogen': 'Xanthomonas oryzae pv. oryzae (Xoo)',
            'pathogen_type': 'bacteria',
            'symptoms': [
                'Lesi kuning kehijauan pada tepi daun',
                'Bercak memanjang berwarna kuning hingga putih keabu-abuan',
                'Eksudat bakteri berwarna kuning pada permukaan lesi (kondisi lembab)',
                'Daun mengering dari ujung ke pangkal',
                'Pada serangan berat, seluruh daun mengering'
            ],
            'favorable_conditions': [
                'Kelembaban tinggi (>80%)',
                'Suhu 25-30°C',
                'Pemupukan nitrogen berlebih',
                'Luka pada daun akibat angin atau serangga',
                'Genangan air yang tinggi'
            ],
            'yield_loss': '20-80%',
            'severity': 'high',
            'treatments': {
                'chemical': [
                    {
                        'name': 'Copper Hydroxide',
                        'brand_examples': ['Kocide 2000', 'Champion WP'],
                        'dosage': '1-2 g/L air',
                        'application': 'Semprot daun saat gejala awal muncul',
                        'interval': 'Setiap 7-10 hari',
                        'notes': 'Bakterisida kontak berbasis tembaga'
                    },
                    {
                        'name': 'Streptomycin Sulfate',
                        'brand_examples': ['Agrept 25 WP', 'Streptomycin'],
                        'dosage': '1-1.5 g/L air',
                        'application': 'Semprot seluruh tajuk tanaman',
                        'interval': 'Setiap 5-7 hari',
                        'notes': 'Antibiotik, hindari penggunaan berlebihan'
                    },
                    {
                        'name': 'Kasugamycin',
                        'brand_examples': ['Kasumin 2L'],
                        'dosage': '1-2 mL/L air',
                        'application': 'Semprot pada pagi atau sore hari',
                        'interval': 'Setiap 7 hari',
                        'notes': 'Efektif untuk bakteri, rendah toksisitas'
                    }
                ],
                'biological': [
                    {
                        'name': 'Bacillus subtilis',
                        'brand_examples': ['Serenade ASO'],
                        'dosage': '5 mL/L air',
                        'application': 'Semprot preventif atau kuratif awal',
                        'notes': 'Agen biokontrol, aman lingkungan'
                    },
                    {
                        'name': 'Paenibacillus polymyxa',
                        'dosage': '5 mL/L air',
                        'application': 'Aplikasi pada tanah dan daun',
                        'notes': 'Bakteri antagonis'
                    }
                ],
                'cultural': [
                    'Gunakan varietas tahan BLB (Inpari 30, Ciherang)',
                    'Kurangi pemupukan nitrogen berlebih',
                    'Atur jarak tanam yang cukup untuk sirkulasi udara',
                    'Drainase sawah yang baik',
                    'Hindari irigasi saat ada serangan',
                    'Musnahkan sisa tanaman terinfeksi',
                    'Rotasi tanaman jika memungkinkan'
                ]
            },
            'prevention': [
                'Gunakan benih bersertifikat bebas penyakit',
                'Perlakuan benih dengan air panas (52°C, 30 menit)',
                'Hindari kerusakan daun saat pemeliharaan',
                'Pengaturan air irigasi yang tepat'
            ]
        },
        
        'brown_spot': {
            'name': 'Brown Spot (Bercak Coklat)',
            'name_id': 'Bercak Coklat',
            'name_en': 'Brown Spot',
            'pathogen': 'Bipolaris oryzae (Cochliobolus miyabeanus)',
            'pathogen_type': 'fungus',
            'symptoms': [
                'Bercak oval hingga bulat berwarna coklat',
                'Bagian tengah bercak berwarna abu-abu',
                'Tepi bercak berwarna coklat kemerahan',
                'Halo kuning di sekitar bercak',
                'Bercak dapat menyatu pada serangan berat',
                'Dapat menyerang biji menyebabkan pecky rice'
            ],
            'favorable_conditions': [
                'Defisiensi nutrisi (N, K, Si)',
                'Tanah masam atau basa',
                'Kelembaban tinggi (86-100%)',
                'Suhu 16-36°C (optimum 25-30°C)',
                'Daun basah selama 8-24 jam'
            ],
            'yield_loss': '5-45%',
            'severity': 'medium',
            'treatments': {
                'chemical': [
                    {
                        'name': 'Propiconazole',
                        'brand_examples': ['Tilt 250 EC', 'Bumper 250 EC'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot saat gejala awal',
                        'interval': 'Setiap 10-14 hari',
                        'notes': 'Fungisida sistemik triazol, sangat efektif'
                    },
                    {
                        'name': 'Azoxystrobin',
                        'brand_examples': ['Amistartop 325 SC'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot preventif atau kuratif',
                        'interval': 'Setiap 14 hari',
                        'notes': 'Fungisida strobilurin, spektrum luas'
                    },
                    {
                        'name': 'Carbendazim',
                        'brand_examples': ['Derosal 500 SC', 'Antracol'],
                        'dosage': '1-2 g/L air',
                        'application': 'Semprot atau rendam benih',
                        'interval': 'Setiap 7-10 hari',
                        'notes': 'Fungisida sistemik benzimidazol'
                    },
                    {
                        'name': 'Mancozeb',
                        'brand_examples': ['Dithane M-45', 'Manzate'],
                        'dosage': '2-3 g/L air',
                        'application': 'Semprot preventif',
                        'interval': 'Setiap 7 hari',
                        'notes': 'Fungisida kontak protektan'
                    },
                    {
                        'name': 'Trifloxystrobin',
                        'brand_examples': ['Nativo 75 WG'],
                        'dosage': '0.3-0.5 g/L air',
                        'application': 'Semprot daun',
                        'interval': 'Setiap 14 hari',
                        'notes': 'Kombinasi strobilurin + triazol'
                    }
                ],
                'biological': [
                    {
                        'name': 'Trichoderma harzianum',
                        'brand_examples': ['Tricho-G', 'SoilGard'],
                        'dosage': '5 g/L air',
                        'application': 'Aplikasi pada tanah dan semprot daun',
                        'notes': 'Jamur antagonis, ramah lingkungan'
                    }
                ],
                'cultural': [
                    'Perbaiki kesuburan tanah dengan pemupukan berimbang',
                    'Tambahkan pupuk kalium (K) dan silika (Si)',
                    'Gunakan varietas tahan (MAC 18)',
                    'Jangan tanam terlalu rapat',
                    'Drainase sawah yang baik',
                    'Bakar jerami terinfeksi setelah panen'
                ]
            },
            'prevention': [
                'Perlakuan benih dengan fungisida atau air panas',
                'Gunakan benih bersertifikat',
                'Hindari defisiensi nutrisi',
                'Rendam benih dalam air dingin 8 jam lalu air panas (53-54°C) 10-12 menit'
            ]
        },
        
        'leaf_blast': {
            'name': 'Leaf Blast (Blas Daun)',
            'name_id': 'Blas Daun',
            'name_en': 'Rice Blast',
            'pathogen': 'Pyricularia oryzae (Magnaporthe oryzae)',
            'pathogen_type': 'fungus',
            'symptoms': [
                'Lesi berbentuk belah ketupat (diamond-shaped)',
                'Bagian tengah berwarna abu-abu hingga putih',
                'Tepi berwarna coklat',
                'Ujung lesi meruncing',
                'Lesi dapat menyatu dan mematikan daun',
                'Dapat menyerang leher malai (neck blast)'
            ],
            'favorable_conditions': [
                'Kelembaban tinggi (>90%)',
                'Suhu sejuk (20-28°C)',
                'Pemupukan nitrogen berlebih',
                'Embun pagi yang lama',
                'Varietas rentan'
            ],
            'yield_loss': '10-100%',
            'severity': 'very_high',
            'treatments': {
                'chemical': [
                    {
                        'name': 'Tricyclazole',
                        'brand_examples': ['Beam 75 WP', 'Blas 75 WP'],
                        'dosage': '1 g/L air',
                        'application': 'Semprot preventif atau saat gejala awal',
                        'interval': 'Setiap 10-14 hari',
                        'notes': 'Fungisida spesifik blast, sangat efektif'
                    },
                    {
                        'name': 'Isoprothiolane',
                        'brand_examples': ['Fuji One 400 EC'],
                        'dosage': '1-2 mL/L air',
                        'application': 'Semprot seluruh tajuk',
                        'interval': 'Setiap 7-10 hari',
                        'notes': 'Fungisida sistemik untuk blast'
                    },
                    {
                        'name': 'Azoxystrobin',
                        'brand_examples': ['Amistartop 325 SC'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot preventif',
                        'interval': 'Setiap 14 hari',
                        'notes': 'Strobilurin spektrum luas'
                    },
                    {
                        'name': 'Propiconazole',
                        'brand_examples': ['Tilt 250 EC'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot saat gejala muncul',
                        'interval': 'Setiap 10-14 hari',
                        'notes': 'Triazol sistemik'
                    },
                    {
                        'name': 'Kasugamycin',
                        'brand_examples': ['Kasumin 2L'],
                        'dosage': '1-2 mL/L air',
                        'application': 'Semprot daun',
                        'interval': 'Setiap 7 hari',
                        'notes': 'Antibiotik fungisida'
                    }
                ],
                'biological': [
                    {
                        'name': 'Trichoderma viride',
                        'dosage': '5 g/L air',
                        'application': 'Semprot preventif',
                        'notes': 'Jamur antagonis'
                    },
                    {
                        'name': 'Bacillus subtilis',
                        'brand_examples': ['Serenade ASO'],
                        'dosage': '5 mL/L air',
                        'application': 'Aplikasi preventif',
                        'notes': 'Biokontrol bakterial'
                    }
                ],
                'cultural': [
                    'Gunakan varietas tahan blast (Ciherang, IR64)',
                    'Kurangi pemupukan nitrogen',
                    'Tanam tidak terlalu rapat',
                    'Pengaturan waktu tanam menghindari musim kondusif',
                    'Manajemen air yang tepat',
                    'Sanitasi lahan dari sisa tanaman'
                ]
            },
            'prevention': [
                'Gunakan benih varietas tahan',
                'Perlakuan benih dengan fungisida',
                'Pemupukan berimbang (tidak berlebih N)',
                'Hindari tanam di musim kondusif blast'
            ]
        },
        
        'leaf_scald': {
            'name': 'Leaf Scald (Lepuh Daun)',
            'name_id': 'Lepuh Daun',
            'name_en': 'Leaf Scald',
            'pathogen': 'Microdochium oryzae (Rhynchosporium oryzae)',
            'pathogen_type': 'fungus',
            'symptoms': [
                'Zona coklat kemerahan hingga coklat gelap pada ujung/tepi daun',
                'Pola zonasi konsentris',
                'Daun tampak seperti terbakar atau lepuh',
                'Garis-garis coklat di antara tulang daun',
                'Daun mengering pada tahap lanjut'
            ],
            'favorable_conditions': [
                'Cuaca sejuk dan lembab',
                'Suhu 22-28°C',
                'Kelembaban tinggi',
                'Penanaman rapat',
                'Nitrogen berlebih'
            ],
            'yield_loss': '10-30%',
            'severity': 'medium',
            'treatments': {
                'chemical': [
                    {
                        'name': 'Propiconazole',
                        'brand_examples': ['Tilt 250 EC', 'Bumper'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot saat gejala awal',
                        'interval': 'Setiap 10-14 hari',
                        'notes': 'Triazol sistemik, sangat efektif'
                    },
                    {
                        'name': 'Tebuconazole',
                        'brand_examples': ['Folicur 250 EC'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot daun',
                        'interval': 'Setiap 14 hari',
                        'notes': 'Triazol sistemik'
                    },
                    {
                        'name': 'Carbendazim',
                        'brand_examples': ['Derosal 500 SC'],
                        'dosage': '1-2 g/L air',
                        'application': 'Semprot preventif/kuratif',
                        'interval': 'Setiap 7-10 hari',
                        'notes': 'Benzimidazol sistemik'
                    },
                    {
                        'name': 'Mancozeb',
                        'brand_examples': ['Dithane M-45'],
                        'dosage': '2-3 g/L air',
                        'application': 'Semprot protektan',
                        'interval': 'Setiap 7 hari',
                        'notes': 'Fungisida kontak'
                    }
                ],
                'biological': [
                    {
                        'name': 'Trichoderma spp.',
                        'dosage': '5 g/L air',
                        'application': 'Aplikasi preventif',
                        'notes': 'Jamur antagonis'
                    }
                ],
                'cultural': [
                    'Gunakan varietas toleran',
                    'Atur jarak tanam yang cukup',
                    'Kurangi nitrogen berlebih',
                    'Drainase yang baik',
                    'Sanitasi sisa tanaman'
                ]
            },
            'prevention': [
                'Perlakuan benih',
                'Pemupukan berimbang',
                'Hindari penanaman terlalu rapat'
            ]
        },
        
        'narrow_brown_spot': {
            'name': 'Narrow Brown Spot (Bercak Coklat Sempit)',
            'name_id': 'Bercak Coklat Sempit',
            'name_en': 'Narrow Brown Leaf Spot (NBLS)',
            'pathogen': 'Cercospora janseana',
            'pathogen_type': 'fungus',
            'symptoms': [
                'Lesi linear sempit berwarna coklat',
                'Lesi sejajar dengan tulang daun',
                'Panjang lesi 2-25 mm, lebar 1-2 mm',
                'Dapat menyerang daun, pelepah, dan malai',
                'Diskolorasi pada gabah'
            ],
            'favorable_conditions': [
                'Penanaman terlambat',
                'Tanaman ratun',
                'Musim semi hangat dan musim panas basah',
                'Kelembaban tinggi'
            ],
            'yield_loss': '8-17%',
            'severity': 'medium',
            'treatments': {
                'chemical': [
                    {
                        'name': 'Propiconazole',
                        'brand_examples': ['Tilt 250 EC'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot saat booting atau heading',
                        'interval': 'Setiap 10-14 hari',
                        'notes': 'Sangat efektif untuk NBLS'
                    },
                    {
                        'name': 'Fluxapyroxad',
                        'brand_examples': ['Priaxor'],
                        'dosage': 'Sesuai label',
                        'application': 'Semprot daun',
                        'interval': 'Setiap 14 hari',
                        'notes': 'SDHI fungisida, efektif untuk NBLS'
                    },
                    {
                        'name': 'Azoxystrobin',
                        'brand_examples': ['Amistartop'],
                        'dosage': '0.5-1 mL/L air',
                        'application': 'Semprot preventif',
                        'interval': 'Setiap 14 hari',
                        'notes': 'Strobilurin'
                    },
                    {
                        'name': 'Benomyl',
                        'brand_examples': ['Benlate'],
                        'dosage': '1-2 g/L air',
                        'application': 'Semprot daun',
                        'interval': 'Setiap 7-10 hari',
                        'notes': 'Benzimidazol sistemik'
                    },
                    {
                        'name': 'Propiconazole + Azoxystrobin',
                        'brand_examples': ['Quilt Xcel'],
                        'dosage': '1 mL/L air',
                        'application': 'Semprot kombinasi',
                        'interval': 'Setiap 14 hari',
                        'notes': 'Kombinasi paling efektif (reduksi 75%)'
                    }
                ],
                'biological': [
                    {
                        'name': 'Trichoderma harzianum',
                        'dosage': '5 g/L air',
                        'application': 'Aplikasi preventif',
                        'notes': 'Jamur antagonis'
                    }
                ],
                'cultural': [
                    'Gunakan varietas tahan/toleran',
                    'Hindari penanaman terlambat',
                    'Rotasi pestisida untuk cegah resistensi',
                    'Manajemen ratun yang baik',
                    'Sanitasi lahan'
                ]
            },
            'prevention': [
                'Tanam tepat waktu',
                'Gunakan varietas toleran',
                'Pemupukan berimbang'
            ]
        },
        
        'healthy': {
            'name': 'Healthy (Sehat)',
            'name_id': 'Daun Sehat',
            'name_en': 'Healthy Leaf',
            'pathogen': None,
            'pathogen_type': None,
            'symptoms': [
                'Daun berwarna hijau segar',
                'Tidak ada bercak atau lesi',
                'Pertumbuhan normal',
                'Tidak ada perubahan warna abnormal'
            ],
            'favorable_conditions': [],
            'yield_loss': '0%',
            'severity': 'none',
            'treatments': {
                'chemical': [],
                'biological': [],
                'cultural': [
                    'Pertahankan pemupukan berimbang',
                    'Lakukan pemantauan rutin setiap minggu',
                    'Jaga kebersihan lahan dari gulma',
                    'Atur pengairan yang tepat',
                    'Perhatikan jarak tanam ideal'
                ]
            },
            'prevention': [
                'Lakukan pemantauan rutin',
                'Pertahankan praktik budidaya yang baik',
                'Siapkan pestisida untuk antisipasi',
                'Catat kondisi tanaman secara berkala'
            ],
            'maintenance_tips': [
                'Monitor tanaman setiap 3-5 hari',
                'Perhatikan perubahan cuaca yang dapat memicu penyakit',
                'Jaga drainase sawah',
                'Aplikasi pupuk sesuai fase pertumbuhan',
                'Bersihkan gulma secara rutin'
            ]
        }
    }
    
    # General Information
    GENERAL_INFO = {
        'application_tips': [
            'Semprot pada pagi hari (06:00-09:00) atau sore hari (15:00-18:00)',
            'Hindari penyemprotan saat hujan atau angin kencang',
            'Gunakan alat pelindung diri (APD) saat aplikasi',
            'Ikuti dosis yang direkomendasikan, jangan berlebihan',
            'Rotasi pestisida dengan mode aksi berbeda untuk cegah resistensi',
            'Periksa label produk untuk informasi keamanan'
        ],
        'safety_precautions': [
            'Gunakan masker, sarung tangan, dan kacamata pelindung',
            'Jangan makan, minum, atau merokok saat aplikasi',
            'Cuci tangan dan badan setelah aplikasi',
            'Simpan pestisida di tempat aman jauh dari jangkauan anak',
            'Jangan buang sisa pestisida ke sumber air'
        ],
        'integrated_pest_management': [
            'Utamakan metode kultur teknis dan varietas tahan',
            'Gunakan pestisida sebagai pilihan terakhir',
            'Kombinasikan pengendalian kimia dan hayati',
            'Monitor populasi musuh alami',
            'Terapkan ambang ekonomi sebelum aplikasi pestisida'
        ]
    }
    
    @classmethod
    def get_disease_info(cls, disease_class):
        """
        Get complete disease information
        
        Args:
            disease_class: Disease class name (e.g., 'bacterial_leaf_blight')
            
        Returns:
            dict: Disease information or None if not found
        """
        # Normalize class name
        normalized = disease_class.lower().replace(' ', '_').replace('-', '_')
        return cls.DISEASES.get(normalized)
    
    @classmethod
    def get_all_diseases(cls):
        """Get list of all disease names"""
        return list(cls.DISEASES.keys())
    
    @classmethod
    def get_treatments(cls, disease_class, treatment_type='all'):
        """
        Get treatments for a disease
        
        Args:
            disease_class: Disease class name
            treatment_type: 'chemical', 'biological', 'cultural', or 'all'
            
        Returns:
            dict or list: Treatment information
        """
        disease = cls.get_disease_info(disease_class)
        if not disease:
            return None
            
        treatments = disease.get('treatments', {})
        
        if treatment_type == 'all':
            return treatments
        else:
            return treatments.get(treatment_type, [])
    
    @classmethod
    def get_general_info(cls):
        """Get general application and safety information"""
        return cls.GENERAL_INFO
