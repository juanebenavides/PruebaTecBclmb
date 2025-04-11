from models.iris import Iris

def get_by_id_range(session, min_id, max_id):
    return session.query(Iris).filter(Iris.id.between(min_id, max_id)).all()

def compare_columns(columns, df_row, db_result_item):
    for i in range(len(columns)):
        db_value = getattr(db_result_item, columns[i])
        if db_value != df_row[columns[i]]:
           return False
    return True

def compare_data(session, df, min_id, max_id):
    db_result = get_by_id_range(session, min_id, max_id)
    filtered_df = df[df['id'].between(min_id, max_id)]
    columns = filtered_df.columns 
    if(len(db_result) != len(filtered_df)):
        print("No se pueden comparar diferentes cantidades de datos")
        return
    for i in range(len(db_result)):
        if not compare_columns(columns, filtered_df.iloc[i], db_result[i]):
            print(f"Datos desiguales en la fila {i}")
            return
    print(f"Datos iguales en el rango de IDs {min_id} - {max_id}")
