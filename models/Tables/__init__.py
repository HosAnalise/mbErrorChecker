import pkgutil
import importlib

# Lista que dirá ao Python e ao Pylance quais nomes podem ser importados deste pacote.
__all__ = []

# Itera recursivamente por todas as subpastas e módulos dentro de 'models/Tables'
for _, module_name, _ in pkgutil.walk_packages(path=__path__, prefix=f'{__name__}.'):
    try:
        # Importa o módulo (ex: 'models.Tables.IntBiAutorizacoes.int_bi_autorizacoes')
        module = importlib.import_module(module_name)
        
        # Procura por classes que sejam modelos SQLAlchemy dentro do arquivo
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            
            # Verifica se o atributo é uma classe de modelo (que tem __tablename__)
            # e se o nome não começa com '_', para evitar importar itens privados.
            if isinstance(attribute, type) and hasattr(attribute, '__tablename__') and not attribute_name.startswith('_'):
                # Disponibiliza o modelo para ser importado diretamente de 'models.Tables'
                globals()[attribute_name] = attribute
                # Adiciona o nome do modelo à nossa lista __all__
                __all__.append(attribute_name)
                
    except Exception as e:
        # Apenas para depuração, caso um arquivo de modelo tenha um erro de sintaxe.
        print(f"Aviso: Erro ao tentar importar o módulo {module_name}: {e}")

# Remove nomes duplicados que possam ter sido adicionados, caso haja.
__all__ = sorted(list(set(__all__)))