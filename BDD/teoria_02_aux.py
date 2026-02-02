import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    "mysql+pymysql://root:Manuel_10@127.0.0.1/cvd",
    future=True
)

archivos = [
    'MEDICAL_DEPARTMENTS.csv',
    'MEDICAL_HISTORY.csv',
    'MEDICAL_LOCATIONS.csv',
    'MEDICAL_PROCEDURES.csv',
    'PATIENTS.csv'
]

columnas = {
    "PATIENTS.csv": [
        "PATIENT_ID","FIRST_NAME","LAST_NAME","SSN",
        "BIRTH_DATE","SEX","ADDRESS","DEPT_ID"
    ],
    "MEDICAL_HISTORY.csv": [
        "MEDICAL_HISTORY_ID","PATIENT_ID","DIAGNOSIS_DATE",
        "DIAGNOSIS_CODE","MEDICAL_CONDITION","DEPT_ID"
    ],
    "MEDICAL_PROCEDURES.csv": [
        "PROCEDURE_ID","PROCEDURE_NAME","PROCEDURE_DATE",
        "PATIENT_ID","DEPT_ID"
    ],
    "MEDICAL_DEPARTMENTS.csv": [
        "DEPT_ID","DEPT_NAME","MANAGER_ID","LOCATION_ID"
    ],
    "MEDICAL_LOCATIONS.csv": [
        "LOCATION_ID","DEPT_ID","LOCATION_NAME"
    ]
}

ruta_base = r'C:\Users\Hp\Documents\GitHub\IBM-Data-Analyst\BDD\utils_02'

print("🚀 Iniciando carga masiva de datos médicos...")

for nombre_archivo in archivos:
    try:
        ruta = os.path.join(ruta_base, nombre_archivo)

        df = pd.read_csv(
            ruta,
            header=None,
            names=columnas[nombre_archivo]
        )

        tabla = nombre_archivo.replace('.csv', '').lower()

        df.to_sql(
            tabla,
            con=engine,
            if_exists='append',
            index=False
        )

        print(f"✅ {tabla} cargada ({len(df)} filas)")

    except Exception as e:
        print(f"❌ Error en {nombre_archivo}: {e}")

print("✨ Proceso terminado")
