import ezdxf

file_path = "antet.dxf"
doc = ezdxf.readfile(file_path)

modelspace = doc.modelspace()

asset_counts = {}
for entity in modelspace:
    asset_name = entity.dxf.get("name", "")
    if asset_name not in asset_counts:
        asset_counts[asset_name] = 1
    else:
        asset_counts[asset_name] += 1

for asset_name, count in asset_counts.items():
    print(f"{asset_name}: {count}")
