import pandas as pd

table_a_path = "table_a.excel"
df_a = pd.read_excel(table_a_path,sheet_name = "Sheet1")
df_a = df_a.drop(df_a.columns[[1,3]],axis=1)

output_path = "table_b.excel"
df_a.to_excel(output_path,sheet_name = "Sheet1",index=False)
print("done!")
