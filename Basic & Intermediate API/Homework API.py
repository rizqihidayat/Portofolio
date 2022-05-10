from flask import request
from flask import Flask
import pandas as pd
import psycopg2 as pg
import numpy as np

def insert_into_table(conn, df, table):
    """
    Using cursor.mogrify() to build the bulk insert query
    then cursor.execute() to execute the query
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]

    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))

    # SQL quert to execute
    cursor = conn.cursor()
    values = [cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", tup).decode('utf8') for tup in tuples]
    print("VALUES", values)
    query = "INSERT INTO %s(%s) VALUES " % (table, cols) + ",".join(values)

    # print("QUERY", query)
    try:
        cursor.execute(query, tuples)
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("INSERT DONE")
    cursor.close()

# set up configuration
host = "localhost"
port = "5432"
database = "postgres"
user = "postgres"
password = "kagome235"
setting = "dbname=" + database + " user=" + user + " host=" + host + " port=" + port + " password=" + password
engine = pg.connect(setting)

application = Flask(__name__)

@application.route('/digital-skola/read-order-items', methods=['GET'])
def read():
    content = request.get_json()
    product_id = content['order_id']
    query = f"""
            select
                *
            from
                order_item_dataset
            where
                1=1
                and order_id = '{order_id}'
            """
    df = pd.read_sql(query, con=engine)
    result = {
        "order_item_id": str(df['order_item_id'].iloc[0]),
        "product_id": int(df['product_id'].iloc[0]),
        "seller_id": int(df['seller_id'].iloc[0]),
        "shipping_limit_date": int(df['shipping_limit_date'].iloc[0]),
        "price": int(df['price'].iloc[0]),
        "freight_value": int(df['freight_value'].iloc[0])
    }
    print("RESULT", result)
    return result

@application.route('/digital-skola/insert-order-items', methods=['POST'])
def insert():
    content = request.get_json()

    order_id = content['order_id']
    order_item_id = content['order_item_id']
    product_id = content['product_id']
    seller_id = content['seller_id']
    shipping_limit_date = content['shipping_limit_date']
    price = content['price']
    freight_value = content['freight_value']

    df = pd.DataFrame()
    df.at[(0,'order_id')] = order_id
    df.at[(0,'order_item_id')] = order_item_id
    df.at[(0,'product_id')] = product_id
    df.at[(0,'seller_id')] = seller_id
    df.at[(0,'shipping_limit_date')] = shipping_limit_date
    df.at[(0,'price')] = price
    df.at[(0,'freight_value')] = freight_value

    insert_into_table(engine, df[:10000], 'order_items_dataset')

    result = {
        "order_item_id": str(df['order_item_id'].iloc[0]),
        "product_id": int(df['product_id'].iloc[0]),
        "seller_id": int(df['seller_id'].iloc[0]),
        "shipping_limit_date": int(df['shipping_limit_date'].iloc[0]),
        "price": int(df['price'].iloc[0]),
        "freight_value": int(df['freight_value'].iloc[0])
    }
    print("RESULT", result)
    return result

if __name__ == '__main__':
    application.run(host='0.0.0.0')