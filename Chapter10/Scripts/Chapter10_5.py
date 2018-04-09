import pyarrow as pa
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": ['c', 'd']})
table = pa.Table.from_pandas(df)
con.load_table_arrow("table_name", table)
df = pd.DataFrame({"A": [1, 2], "B": ["c", "d"]})
con.load_table_columnar("table_name", df, preserve_index=False)
data = [(1, "c"), (2, "d")]
con.load_table("table_name", data)