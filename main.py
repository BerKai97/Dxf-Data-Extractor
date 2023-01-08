import ezdxf
import pandas as pd
import csv

class DDE:
    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = ezdxf.readfile(file_path)
        self.modelspace = self.doc.modelspace()
        self.asset_counts = {}

    def count_assets(self):
        try:
            self.asset_counts = {}
            for entity in self.modelspace:
                asset_name = entity.dxfattribs().get('name')
                if asset_name not in self.asset_counts:
                    self.asset_counts[asset_name] = 1
                else:
                    self.asset_counts[asset_name] += 1
                
            # pandas <3
            df = pd.DataFrame(list(self.asset_counts.items()), columns=['Asset', 'Count'])
            df.to_csv(f'{self.file_path}_asset_counts.csv', index=False)

            # try:
            #     os.startfile(os.path.dirname(self.file_path))
            # except Exception as e:
            #     print(e)
            #     pass
            return True


        except Exception as e:
            # print(e)
            return False

    def calculate_price(self, price_csv):
        not_found = []
        cost = 0
        csvfile = open(price_csv, 'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            asset_name = row['Asset']
            asset_price = row['Price']
            # asset_price_type = row['Type']
            if asset_name in self.asset_counts:
                cost += float(asset_price) * self.asset_counts[asset_name]
            
        # Sometimes the asset name in the csv file is different from the one in the dxf file,
        # because of this, we need to check if the asset name is in the price file
        # and report that to the user
        for asset_name in self.asset_counts:
            if asset_name not in reader.fieldnames:
                not_found.append(asset_name)

        # Exporting cost and not found list to a text file
        with open(f'{self.file_path}_cost.txt', 'w') as f:
            f.write(f'Cost: {cost}\n')
            f.write('Not found:\n')
            for asset_name in not_found:
                f.write(f'{asset_name}\n')


        


        csvfile.close()

        # TODO entegrate cost message and report
        return cost


if __name__ == '__main__':
    pass

