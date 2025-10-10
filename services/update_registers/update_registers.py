from services.bussines_logic.error_analysis_service import ErrorAnalysis
import logging

logging.basicConfig(level=logging.INFO)





def update_registers(error_list: list, erro_analyze: ErrorAnalysis = ErrorAnalysis(),agent=None) -> bool:

    try:

        if not error_list:
            logging.info("No errors found")
            return
        
        table_name = ""
        grouped_errors = erro_analyze.group_error_by_table(error_list)
       
        for error_group in grouped_errors.errors:

            table_errors = [{error.table_name: error.erro} for error in error_group.error]

            agent.run([erro.values() for erro in table_errors])

            table_name = error_group.error[0].table_name
            logging.info(f"\n--- Process table: {table_name} ---")        

    except Exception as e:
        logging.error(f"An unexpected error occurred while processing table {table_name}: {e} ", exc_info=True)
        return False        

if __name__ == "__main__":
    update_registers()