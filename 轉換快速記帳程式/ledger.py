import json
import pandas as pd
import os
import datetime as dt
import numpy as np


class Ledger:

    def __init__(self):
        pass

    def main(self):

        input_filename = 'Ahorro_Backup_20200402223058.json'
        
        input_file_date = input_filename.split('_')[2].split('.')[0]
        input_file_date = dt.datetime.strptime(input_file_date, '%Y%m%d%H%M%S')
        
        main_file_name = 'Export(' + input_file_date.strftime("%Y-%m-%d %H-%M-%S") + ')'
        if not os.path.isdir(main_file_name):
            os.makedirs(main_file_name)
        
        with open(input_filename, 'r', encoding="utf8") as reader:
            inputJson = json.loads(reader.read())
        
        icon_id_dict = {}
        icon_to_chi_dict = {}
        for item in inputJson['tables'][4]['items']:
            if item['behavior'] == 'expense':
                if item['icon'] == 'bread':
                    icon_to_chi_dict.update({item['icon']:"早餐"})
                elif item['icon'] == 'lunch':
                    icon_to_chi_dict.update({item['icon']:"午餐"})
                elif item['icon'] == 'dinner':
                    icon_to_chi_dict.update({item['icon']:"晚餐"})
                elif item['icon'] == 'drink':
                    icon_to_chi_dict.update({item['icon']:"飲料"})
                elif item['icon'] == 'candy':
                    icon_to_chi_dict.update({item['icon']:"零食"})
                elif item['icon'] == 'traffic':
                    icon_to_chi_dict.update({item['icon']:"交通"})
                elif item['icon'] == 'grocery':
                    icon_to_chi_dict.update({item['icon']:"日常用品"})
                elif item['icon'] == 'entertainment':
                    icon_to_chi_dict.update({item['icon']:"娛樂"})
                elif item['icon'] == 'social':
                    icon_to_chi_dict.update({item['icon']:"社交"})
                elif item['icon'] == 'cloth':
                    icon_to_chi_dict.update({item['icon']:"衣物"})
                elif item['icon'] == 'shopping':
                    icon_to_chi_dict.update({item['icon']:"購物"})
                elif item['icon'] == 'rent':
                    icon_to_chi_dict.update({item['icon']:"房租"})
                elif item['icon'] == 'gift':
                    icon_to_chi_dict.update({item['icon']:"禮物"})
                elif item['icon'] == 'red_envelope':
                    icon_to_chi_dict.update({item['icon']:"禮金"})
                elif item['icon'] == 'hospital':
                    icon_to_chi_dict.update({item['icon']:"醫療"})
                elif item['icon'] == 'phone':
                    icon_to_chi_dict.update({item['icon']:"電話費"})
                elif item['icon'] == 'stock':
                    icon_to_chi_dict.update({item['icon']:"投資"})
                elif item['icon'] == 'visa':
                    icon_to_chi_dict.update({item['icon']:"信用卡"})
                elif item['icon'] == 'transfer':
                    icon_to_chi_dict.update({item['icon']:"轉帳"})
                elif item['icon'] == 'other':
                    icon_to_chi_dict.update({item['icon']:"其他"})
                icon_id_dict.update({item['_id']:item['icon']})
        
        
        
        
        
        have_not_dir_name_dict = {}
        index_date = dt.datetime.strptime('1970-01-01', '%Y-%m-%d')
        for item in inputJson['tables'][0]['items']:
            loop_date = item['date']
            loop_date = dt.datetime.strptime(loop_date, '%Y-%m-%d')
            if (loop_date.month != index_date.month) or (loop_date.year != index_date.year):
                index_date = loop_date
                dir_name = index_date.strftime('%Y-%m')
                have_not_dir_name_dict.update({dir_name:True})
        
        
        excel_writer_dict = {}
        book_table_dict = {}
        icon_table_dict = {}
        json_item = inputJson['tables'][0]['items']
        for index in range(len(json_item)):
            print(json_item[index]['date'])
            loop_date = dt.datetime.strptime(json_item[index]['date'], '%Y-%m-%d')
            dir_name = loop_date.strftime('%Y-%m')
            
            # 如果 這個月 沒建過檔 就要建檔
            if have_not_dir_name_dict[dir_name]:
                have_not_dir_name_dict[dir_name] = False
                if not os.path.isdir(main_file_name + '/' + dir_name):
                    os.makedirs(main_file_name + '/' + dir_name)
                
                book_table = {
                    '日期':[],
                    '帳戶':[],
                    '類型':[],
                    '描述':[],
                    '金額':[],
                    }
                book_table_dict.update({ dir_name:book_table })
                
                excel_file_name = main_file_name + '/' + dir_name + '/' + 'detail.xlsx'
                excel_writer_dict.update({dir_name:pd.ExcelWriter(excel_file_name, engine='xlsxwriter')})
            # 如果 這個月 沒建過檔 就要建檔
            
        
            val_date = ''
            val_account_id = ''
            val_category_id = ''
            val_descr = ''
            val_amount = 0
            
            val_date = json_item[index]['date']
            
            if json_item[index]['account_id'] == '1':
                val_account_id = '生活費'
            elif json_item[index]['account_id'] == '4':
                val_account_id = '非生活費'
            else:
                val_account_id = json_item[index]['account_id']
            
            val_category_id = icon_to_chi_dict[icon_id_dict[json_item[index]['category_id']]]
            val_descr = json_item[index]['descr']
            val_amount = int(json_item[index]['amount'])
            
            book_table_dict[dir_name]
            book_table_dict[dir_name]['日期'].append(val_date)
            book_table_dict[dir_name]['帳戶'].append(val_account_id)
            book_table_dict[dir_name]['類型'].append(val_category_id)
            book_table_dict[dir_name]['描述'].append(val_descr)
            book_table_dict[dir_name]['金額'].append(val_amount)
        
        
        
        for item in excel_writer_dict:
            book_table_DF = pd.DataFrame(book_table_dict[item])
            life_meals_cost_DF = pd.DataFrame(book_table_DF[book_table_DF['帳戶'] == '生活費'].reset_index(drop=True))
        
            # =========================================================================
            category_total_dict = {
                    '類型': [],
                    '金額': [],
                    '比例': [],
                    }
            for category_str in icon_to_chi_dict.values():
                category_total = life_meals_cost_DF[life_meals_cost_DF['類型'] == category_str]['金額'].sum()
                category_all_total = life_meals_cost_DF['金額'].sum()
                category_total_dict['類型'].append(category_str)
                category_total_dict['金額'].append(category_total)
                category_total_dict['比例'].append( round((category_total / category_all_total), 4) )
            category_total_DF = pd.DataFrame(category_total_dict).sort_values(by=['比例'], ascending=False).reset_index(drop=True)
            category_total_DF.to_excel(excel_writer_dict[item], sheet_name='花費比例(生活費)', encoding='utf8')
            # =========================================================================
            
        
            # =========================================================================
            life_meals_cost_DF = pd.DataFrame(book_table_DF[book_table_DF['帳戶'] == '生活費'].reset_index(drop=True))
            meals_detail_DF = life_meals_cost_DF[
                    (life_meals_cost_DF['類型'] == '早餐') | 
                    (life_meals_cost_DF['類型'] == '午餐') | 
                    (life_meals_cost_DF['類型'] == '晚餐')]
            life_cost_DF = life_meals_cost_DF.drop(meals_detail_DF.index).reset_index(drop=True)
            life_cost_meals_total_DF = life_cost_DF.append(pd.DataFrame({
                    '日期': [np.nan],
                    '帳戶': [np.nan],
                    '類型': [np.nan],
                    '描述': ['總計'],
                    '金額': [life_cost_DF['金額'].sum()],
                    }), ignore_index=True)
            life_cost_meals_total_DF.to_excel(excel_writer_dict[item], sheet_name='明細(不含餐飲費)', encoding='utf8')
            # =========================================================================
        
            
            # =========================================================================
            meals_total_DF = category_total_DF[
                    (category_total_DF['類型'] == '早餐') |
                    (category_total_DF['類型'] == '午餐') |
                    (category_total_DF['類型'] == '晚餐') ].drop(columns=['比例']).reset_index(drop=True)
            meals_total_DF = meals_total_DF.append(pd.DataFrame({
                    '類型': [np.nan],
                    '金額': [meals_total_DF['金額'].sum()],
                    }), ignore_index=True)
            meals_total_DF.to_excel(excel_writer_dict[item], sheet_name='明細(餐飲費)', encoding='utf8')
            # =========================================================================
            
            
            # =========================================================================
            book_table_total_DF = book_table_DF.append(pd.DataFrame({
                    '日期': [np.nan],
                    '帳戶': [np.nan],
                    '類型': [np.nan],
                    '描述': ['總計'],
                    '金額': [book_table_DF['金額'].sum()],
                    }), ignore_index=True)
            book_table_total_DF.to_excel(excel_writer_dict[item], sheet_name='明細(全部)', encoding='utf8')
            # =========================================================================
        
            excel_writer_dict[item].save()



if __name__ == '__main__':
    Ledger().main()
