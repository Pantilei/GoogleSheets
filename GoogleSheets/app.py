from fastapi import FastAPI
from services import spreadsheet
app = FastAPI()


@app.get("/")
async def root():

    return {"message": spreadsheet.sheet_1.get_all_records()}


@app.put("/set-value/{row_number}")
async def set_value(row_number: int):
    sheet_3_first_row_values = spreadsheet.sheet_3.row_values(row_number+1)
    sheet_2_first_row_values = spreadsheet.sheet_2.row_values(row_number+1)
    # Delete the processed row
    spreadsheet.sheet_3.delete_row(row_number+1)
    spreadsheet.sheet_2.delete_row(row_number+1)
    # Update status cell
    spreadsheet.update_status_cell()
    return ":".join(sheet_3_first_row_values)
    # return {
    #     "sheet_3_first_row": sheet_3_first_row_values,
    #     "sheet_2_first_row": sheet_2_first_row_values
    # }
