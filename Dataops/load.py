import pandas as pd
from googleapiclient.discovery import build
from sqlalchemy import create_engine, inspect
import os
import transform

def load_youtube_data():
    df_new=transform.tranform_youtube_data() 
    # csv_file_path = "youtube_data.csv"
    # if os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0:
    #     print("CSV file exists and is not empty")
    #     with open(csv_file_path, 'r') as file:
    #          file_content = file.read()
    #          print("Content of the CSV file:")
    #          print(file_content)
    #     df_existing = pd.read_csv(csv_file_path)
    #     print("Columns in existing DataFrame:", df_existing.columns)
    # else:
    #     print("CSV file does not exist or is empty")
    #     df_existing = pd.DataFrame()

    # df_combined = pd.concat([df_existing, df_new])
    csv_file_path = "youtube_data.csv"

    # Check if the CSV file exists and is not empty
    if os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0:
        print("CSV file exists and is not empty")
        df_existing = pd.read_csv(csv_file_path)
        print("Columns in existing DataFrame:", df_existing.columns)
    else:
        print("CSV file does not exist or is empty")
        df_existing = pd.DataFrame()

    # Combine existing data with new data
    df_combined = pd.concat([df_existing, df_new])

    # Save combined data to CSV
    df_combined.to_csv(csv_file_path, index=False)

    # MySQL database connection 
    db_username = 'root'
    db_password = 'root'
    db_host = 'localhost'
    db_name = 'airflow_data'

    # Create SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}")

    # Check if the table exists
    inspector = inspect(engine)
    if inspector.has_table('youtube_videos'):
        df_mysql_existing = pd.read_sql_table('youtube_videos', con=engine)
        df_mysql_combined = pd.concat([df_mysql_existing, df_new])
    else:
        df_mysql_combined = df_new

    # Load combined data into MySQL table
    df_mysql_combined.to_sql('youtube_videos', con=engine, if_exists='replace', index=False)

    # Close database connection
    engine.dispose()

# Call the function 
load_youtube_data()
