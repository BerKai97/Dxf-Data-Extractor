import ezdxf
import pandas as pd
import csv
import os

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

            # csv writer (pandas is better)
            # with open(f'{self.file_path}_asset_counts.csv', 'w', newline='') as csvfile:
            #     fieldnames = ['Asset', 'Count']
            #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #     writer.writeheader()
            #     for asset_name, count in self.asset_counts.items():
            #         writer.writerow({'Asset': asset_name, 'Count': count})

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
            

        csvfile.close()

        # TODO entegrate cost message and report
        return cost


if __name__ == '__main__':
    pass

