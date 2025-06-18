# Definir las opciones de los campos de selección en un solo archivo
ESTADO_CHOICES = [
    ('No Procede', 'No Procede'),
    ('Presentar a CBT', 'Presentar a CBT'),
    ('Presentar a CBN', 'Presentar a CBN'),
    ('Espera respuesta CBN', 'Espera respuesta CBN'),
    ('Aprobado por CBT', 'Aprobado por CBT'),
    ('Aprobado por CBN', 'Aprobado por CBN'),
    ('No aprobado (reubicar)', 'No aprobado (reubicar)'),    
    ('No aprobado', 'No aprobado'),   
    ('Espera firma anexo0', 'Espera firma anexo0'), 
    ('Espera firma anexoA', 'Espera firma anexoA'), 
    ('Firmado Anexo0', 'Firmado Anexo0'), 
    ('Asignar Responsable', 'Asignar Responsable'), 
]

MOTIVO_BAJA_CHOICES = [
    ('Obsolescencia', 'Obsolescencia'),
    ('deterioro', 'Deterioro'),
]

DESTINO_FINAL_CHOICES = [  
    ('materia prima', 'Materia Prima'),  
    ('radioaficionados', 'Radioaficionados'),
    ('otro', 'Otro'),
]

ANEXOS_CHOICES = [
    ('no', 'No'),
    ('si', 'Si'),    
]

UNIDAD_ORGANIZATIVA_CHOICES = [
    ('DTAR, Dirección', 'DTAR, Dirección'),
    ('DTAR, Dpto. Coordinación General', 'DTAR, Dpto. Coordinación General'),
    ('DTAR, Dpto. Economía', 'DTAR, Dpto. Economía'),
    ('DTAR, Dpto. Capital Humano', 'DTAR, Dpto. Capital Humano'),
    ('DTAR, Dpto. Centro de Dirección Territorial', 'DTAR, Dpto. Centro de Dirección Territorial'),
    ('DTAR, Dpto. Logística y Servicios, Grupo Logística', 'DTAR, Dpto. Logística y Servicios, Grupo Logística'),
    ('DTAR, Dpto. Logística y Servicios', 'DTAR, Dpto. Logística y Servicios'),
    ('DTAR, Dpto. Logística y Servicios, Grupo Servicios Generales', 'DTAR, Dpto. Logística y Servicios, Grupo Servicios Generales'),
    ('DTAR, Dpto. Logística y Servicios, Grupo Transporte', 'DTAR, Dpto. Logística y Servicios, Grupo Transporte'),
    ('DTAR, Dpto. TI', 'DTAR, Dpto. TI'),
    ('DTAR, Dpto. Comercial', 'DTAR, Dpto. Comercial'),
    ('DTAR, Dpto. Inversiones', 'DTAR, Dpto. Inversiones'),
    ('DTAR, Dpto. Operaciones de la Red', 'DTAR, Dpto. Operaciones de la Red'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Administración de la Red', 'DTAR, Dpto. Operaciones de la Red, Grupo Administración de la Red'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Operativa', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Operativa'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Fibra Óptica', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Fibra Óptica'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Control de la Operación', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Control de la Operación'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Transmisión', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Transmisión'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Tráfico y Optimización', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Tráfico y Optimización'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Supervisión', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Supervisión'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Control', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Control'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Energética, Clima y SPI', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Energética, Clima y SPI'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Pizarras Privadas', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Pizarras Privadas'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Redes Inalámbricas', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Redes Inalámbricas'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad COCC13', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad COCC13'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Logística y Talleres', 'DTAR, Dpto. Operaciones de la Red, Grupo Logística y Talleres'),
    ('DTAR, CTP Artemisa', 'DTAR, CTP Artemisa'),
    ('DTAR, CTP Artemisa, CTA Guanajay', 'DTAR, CTP Artemisa, CTA Guanajay'),
    ('DTAR, CTP Artemisa, CTA Caimito', 'DTAR, CTP Artemisa, CTA Caimito'),
    ('DTAR, CTP ZEDM', 'DTAR, CTP ZEDM'),
    ('DTAR, CTP ZEDM, CTA Mariel', 'DTAR, CTP ZEDM, CTA Mariel'),
    ('DTAR, CTP Guira de Melena', 'DTAR, CTP Guira de Melena'),
    ('DTAR, CTP Guira de Melena, CTA San Antonio de los Baños', 'DTAR, CTP Guira de Melena, CTA San Antonio de los Baños'),
    ('DTAR, CTP Guira de Melena, CTA Bauta', 'DTAR, CTP Guira de Melena, CTA Bauta'),
    ('DTAR, CTP Guira de Melena, CTA Alquizar', 'DTAR, CTP Guira de Melena, CTA Alquizar'),
    ('DTAR, CTP San Cristobal', 'DTAR, CTP San Cristobal'),
    ('DTAR, CTP San Cristobal, CTA Candelaria', 'DTAR, CTP San Cristobal, CTA Candelaria'),
    ('DTAR, CTP San Cristobal, CTA Bahia Honda', 'DTAR, CTP San Cristobal, CTA Bahia Honda'),
]

DETALLES_CHOICES = [
    ('DETERIORADO ÚTIL', 'DETERIORADO ÚTIL'),
    ('DETERIORADO NO ÚTIL', 'DETERIORADO NO ÚTIL'),    
    ('OBSOLETO REUTILIZABLE', 'OBSOLETO REUTILIZABLE'),    
    ('OBSOLETO NO REUTILIZABLE', 'OBSOLETO NO REUTILIZABLE'),    
]
ESTADO_ACTUAL_CHOICES = [
    ('Malo', 'Malo'),
    ('Regular', 'Regular'),
    ('Bueno', 'Bueno'), 
]
RECHAZADA_CHOICES = [
    ('False', 'No'),
    ('True', 'Si'),    
]

AREA_PERTENECE = [
    ('DTAR, Dirección', 'DTAR, Dirección'),
    ('DTAR, Dpto. Coordinación General', 'DTAR, Dpto. Coordinación General'),
    ('DTAR, Dpto. Economía', 'DTAR, Dpto. Economía'),
    ('DTAR, Dpto. Capital Humano', 'DTAR, Dpto. Capital Humano'),
    ('DTAR, Dpto. Centro de Dirección Territorial', 'DTAR, Dpto. Centro de Dirección Territorial'),
    ('DTAR, Dpto. Logística y Servicios, Grupo Logística', 'DTAR, Dpto. Logística y Servicios, Grupo Logística'),
    ('DTAR, Dpto. Logística y Servicios', 'DTAR, Dpto. Logística y Servicios'),
    ('DTAR, Dpto. Logística y Servicios, Grupo Servicios Generales', 'DTAR, Dpto. Logística y Servicios, Grupo Servicios Generales'),
    ('DTAR, Dpto. Logística y Servicios, Grupo Transporte', 'DTAR, Dpto. Logística y Servicios, Grupo Transporte'),
    ('DTAR, Dpto. TI', 'DTAR, Dpto. TI'),
    ('DTAR, Dpto. Comercial', 'DTAR, Dpto. Comercial'),
    ('DTAR, Dpto. Inversiones', 'DTAR, Dpto. Inversiones'),
    ('DTAR, Dpto. Operaciones de la Red', 'DTAR, Dpto. Operaciones de la Red'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Administración de la Red', 'DTAR, Dpto. Operaciones de la Red, Grupo Administración de la Red'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Operativa', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Operativa'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Fibra Óptica', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Fibra Óptica'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Control de la Operación', 'DTAR, Dpto. Operaciones de la Red, Grupo Red de Acceso, Unidad Control de la Operación'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Transmisión', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Transmisión'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Tráfico y Optimización', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Tráfico y Optimización'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Supervisión', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Supervisión'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Control', 'DTAR, Dpto. Operaciones de la Red, Grupo Supervisión y Gestión, Unidad de Control'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Energética, Clima y SPI', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Energética, Clima y SPI'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Pizarras Privadas', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Pizarras Privadas'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Redes Inalámbricas', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad Redes Inalámbricas'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad COCC13', 'DTAR, Dpto. Operaciones de la Red, Grupo Intervención Técnica, Unidad COCC13'),
    ('DTAR, Dpto. Operaciones de la Red, Grupo Logística y Talleres', 'DTAR, Dpto. Operaciones de la Red, Grupo Logística y Talleres'),
    ('DTAR, CTP Artemisa', 'DTAR, CTP Artemisa'),
    ('DTAR, CTP Artemisa, CTA Guanajay', 'DTAR, CTP Artemisa, CTA Guanajay'),
    ('DTAR, CTP Artemisa, CTA Caimito', 'DTAR, CTP Artemisa, CTA Caimito'),
    ('DTAR, CTP ZEDM', 'DTAR, CTP ZEDM'),
    ('DTAR, CTP ZEDM, CTA Mariel', 'DTAR, CTP ZEDM, CTA Mariel'),
    ('DTAR, CTP Guira de Melena', 'DTAR, CTP Guira de Melena'),
    ('DTAR, CTP Guira de Melena, CTA San Antonio de los Baños', 'DTAR, CTP Guira de Melena, CTA San Antonio de los Baños'),
    ('DTAR, CTP Guira de Melena, CTA Bauta', 'DTAR, CTP Guira de Melena, CTA Bauta'),
    ('DTAR, CTP Guira de Melena, CTA Alquizar', 'DTAR, CTP Guira de Melena, CTA Alquizar'),
    ('DTAR, CTP San Cristobal', 'DTAR, CTP San Cristobal'),
    ('DTAR, CTP San Cristobal, CTA Candelaria', 'DTAR, CTP San Cristobal, CTA Candelaria'),
    ('DTAR, CTP San Cristobal, CTA Bahia Honda', 'DTAR, CTP San Cristobal, CTA Bahia Honda'),
]

#FALTA AGREGARCHOICES PARA UNIDAD ORGANIZATIVA