from classes.Drain3 import Drain3Miner

drain3_miner = Drain3Miner()

def get_templates():
    return drain3_miner.template_miner.drain.clusters





if __name__ == "__main__":
    templates = get_templates()
    for template in templates:
        print(template)