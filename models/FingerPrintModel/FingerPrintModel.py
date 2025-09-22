from pydantic import BaseModel, Field





class FingerPrintModel(BaseModel):
    change_type: str = Field(..., description="Tipo de alteração do fingerprint")
    cluster_id: int = Field(..., description="ID do cluster onde o erro ocorreu")
    cluster_size: int = Field(..., description="Tamanho do cluster")
    template_mined: str = Field(..., description="Template extraído do erro")
    cluster_count: int = Field(..., description="Contagem de clusters")