import ezdxf
import pandas as pd

class AssetCounter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = ezdxf.readfile(file_path)
        self.modelspace = self.doc.modelspace()

    def count_assets(self):
        try:
            asset_counts = {}
            for entity in self.modelspace:
                asset_name = entity.dxfattribs().get('name')
                if asset_name not in asset_counts:
                    asset_counts[asset_name] = 1
                else:
                    asset_counts[asset_name] += 1

            # for asset_name, count in asset_counts.items():
            #     print(f"{asset_name}: {count}")
            
            
            df = pd.DataFrame(list(asset_counts.items()), columns=['Asset', 'Count'])
            df.to_csv(f'{self.file_path}_asset_counts.csv', index=False)
            return True

        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    pass
    # file_path = "antet.dxf"
    # asset_counter = AssetCounter(file_path)
    # asset_counter.count_assets()
