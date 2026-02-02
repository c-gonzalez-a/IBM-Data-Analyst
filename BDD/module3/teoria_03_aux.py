import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    "mysql+pymysql://root:Manuel_10@127.0.0.1/hr",
    future=True
)

archivos = [
    'Departments.csv',
    'Employees.csv',
    'Jobs.csv',
    'JobsHistory.csv',
    'Locations.csv'
]

columnas = {
    "Employees.csv": [
        "EMP_ID","F_NAME","L_NAME","SSN",
        "B_DATE","SEX","ADDRESS","JOB_ID","SALARY","MANAGER_ID","DEP_ID"
    ],
    "JobsHistory.csv": [
        "EMPL_ID","START_DATE","JOBS_ID","DEPT_ID"
    ],
    "Jobs.csv": [
        "JOB_IDENT","JOB_TITLE","MIN_SALARY","MAX_SALARY"
    ],
    "Departments.csv": [
        "DEPT_ID_DEP","DEP_NAME","MANAGER_ID","LOC_ID"
    ],
    "Locations.csv": [
        "LOCT_ID","DEP_ID_LOC"
    ]
}

ruta_base = r'C:\Users\Hp\Documents\GitHub\IBM-Data-Analyst\BDD\module3\utils_03'

print("🚀 Iniciando carga masiva de datos HR...")

for nombre_archivo in archivos:
    try:
        ruta = os.path.join(ruta_base, nombre_archivo)

        df = pd.read_csv(
            ruta,
            header=None,
            names=columnas[nombre_archivo]
        )

        tabla = nombre_archivo.replace('.csv', '')

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