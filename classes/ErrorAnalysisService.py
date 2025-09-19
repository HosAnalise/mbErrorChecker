from models.ErrorModel.ErrorModel import ErrorModel, ErrorListModel
from models.DbModel.QueryReturnModel import QueryReturnModel
from collections import defaultdict
from pydantic_ai.agent import RunContext




class ErrorAnalysisService:   
    
    @staticmethod
    def group_errors_by_store(ctx: RunContext) -> ErrorListModel:
        """
        Group errors by store code.

        Args:
            errors (list[QueryReturnModel]): List of query return models.

        Returns:
            ErrorListModel: Object with store code as key and list of errors as value.
        """
        grouped_errors = defaultdict(list)
        list_errors = ctx

<<<<<<< HEAD
        for error in errors:
            grouped_errors[error.empresa].append(error)
=======


        for error in list_errors:

            grouped_errors[error.store].append(error)
>>>>>>> aa0f29fff87fd11ec2acd0c38ec36129aef8bb7b

  
        return ErrorListModel(
            errors=[
                ErrorModel(
                    error=value,
                    store=key,
                    count=len(value)
                ) for key,value in grouped_errors.items()
            ]
        )
        
   
