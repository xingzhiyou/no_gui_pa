import pandas as pd
import paweb


class StS:
    def __init__(self):
        pass

    def savests(self):
        paw = paweb.PaWeb()
        house_data = paw.llist(1)
        for n in range(2, 4):
            house_data += paw.llist(n)
        df = pd.DataFrame(house_data)
        df.to_csv('my_file.csv', index=False, header=True)
