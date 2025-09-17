from models.ErrorModel.ErrorModel import ErrorModel, ErrorListModel
from models.DbModel.QueryReturnModel import QueryReturnModel
from collections import defaultdict
from pydantic_ai import Agent





class ErrorAnalysisService:
   
    
    @staticmethod
    def group_errors_by_store(errors: list[QueryReturnModel]) -> ErrorListModel:
        """
        Group errors by store code.

        Args:
            errors (list[QueryReturnModel]): List of query return models.

        Returns:
            ErrorListModel: Object with store code as key and list of errors as value.
        """
        grouped_errors = defaultdict(list)

        for error in errors:
            grouped_errors[error.code].append(error)

  
        return ErrorListModel(
            errors=[
                ErrorModel(
                    error=value,
                    store=key,
                    count=len(value)
                ) for key,value in grouped_errors.items()
            ]
        )
        
   
