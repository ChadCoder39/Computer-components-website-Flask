from readJson import readJson
import os


def cartDataByProdIds(ids: [int]):
    dataFolderPath = os.path.join(os.path.dirname(__file__), '..', 'data')

    data = []
    for filename in os.listdir(dataFolderPath):
        filePath = os.path.join(dataFolderPath, filename)

        with open(filePath) as file:
            data.extend(json.load(file))

    return [product for product in data if product['product_id'] in ids]