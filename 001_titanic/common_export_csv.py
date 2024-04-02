import csv


def export_csv_datasets(data_sets,file_name='output_price_lists.csv', encodings='SJIS')-> None:
        with open(file_name, 'w', newline='', encoding=encodings) as csvfile:
            csvwriter = csv.writer(csvfile)
            # 出力配列の各要素を処理してCSVに書き込む
            print(data_sets)
            csvwriter.writerow(data_sets)
            # for item in data_sets:
            #     # カンマ区切りの文字列をリストに分割します
            #     row = item#.split(',')
            #     print(row)
            #     # CSVに書き込みます
            #     csvwriter.writerow(row)