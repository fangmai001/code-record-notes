import pandas as pd
import csv

csv_df = pd.read_csv('ect_ECTT0007_unit.csv')

csv_df = csv_df.drop(columns=[
                            'module_power',
                            'inverter_model',
                            'inverter_serial_number',
                            'tilt',
                            'orientation',
                            'orientation_azimuth',
                            'remark',
                            'sensor_model',
                            ])

csv_df = csv_df[[
                'PLANT_NO', 
                'UNIT_ID',
                'POWER_COLLECTOR_KEY',
                'UNIT_TYPE',
                'DESCRIPTION',
                'CATEGORY',
                'UNIT_SN',
                'SPECIFICATION',
                'WITH_DC',
                'CAPACITY',
                'facing',
                'INV_RSID',
                'INV_SN',
                'INV_NO',
                'INV_SIZE',
                'MPPT',
                'STRING_QTY',
                'ARRAY_QTY',
                'MODULE_QTY',
                'MPPT_RELATION',
                ]]

csv_main_df = csv_df

# ======================================================================
# ======================================================================
# ======================================================================

csv_df = pd.read_csv('ect_active_plants_units_20200303.csv')

csv_df = csv_df.drop(columns=[
                            'PHYSICAL_ADDRESS',
                            'VENDOR',
                            'CREATE_TIME',
                            'LM_USER',
                            'LM_TIME',
                            'DUMMY_FLAG',
                            'DEVICE_TREE_ID',
                            'CREATE_USER',
                            'check_coefficient',
                            'VMPP',
                            'IMPP',
                            'UPDATE_FLAG',
                            'db_updated_at'
                            ])

csv_df = csv_df[[
                'PLANT_NO',
                'UNIT_ID',
                'POWER_COLLECTOR_KEY',
                'UNIT_TYPE',
                'DESCRIPTION',
                'CATEGORY',
                'UNIT_SN',
                'SPECIFICATION',
                'WITH_DC',
                'CAPACITY',
                'facing',
                'INV_RSID',
                'INV_SN',
                'INV_NO',
                'INV_SIZE',
                'MPPT',
                'STRING_QTY',
                'ARRAY_QTY',
                'MODULE_QTY',
            ]]

csv_main_df = csv_main_df.append(csv_df, ignore_index=True)


# ======================================================================
# ======================================================================
# ======================================================================

csv_main_df = csv_main_df[[
                'PLANT_NO', 
                'UNIT_ID',
                'POWER_COLLECTOR_KEY',
                'UNIT_TYPE',
                'DESCRIPTION',
                'CATEGORY',
                'UNIT_SN',
                'SPECIFICATION',
                'WITH_DC',
                'CAPACITY',
                'facing',
                'INV_RSID',
                'INV_SN',
                'INV_NO',
                'INV_SIZE',
                'MPPT',
                'STRING_QTY',
                'ARRAY_QTY',
                'MODULE_QTY',
                'MPPT_RELATION',
                ]]

csv_main_df.to_csv(r'ect_active_plants_units_20200318.csv', quotechar='"', quoting=csv.QUOTE_ALL, index=False)


csv_df = pd.read_csv('ect_active_plants_units_20200318.csv')
csv_df = csv_df.fillna('NULL')
csv_df['WITH_DC'] = csv_df['WITH_DC'].astype(str)
for index in range(csv_df['WITH_DC'].size):
    if csv_df['WITH_DC'][index] == 'False':
        # csv_df.at[index, 'WITH_DC'] = 'FALSE'
        csv_df['WITH_DC'][index] = 'FALSE'
    if csv_df['WITH_DC'][index] == 'True':
        # csv_df.at[index, 'WITH_DC'] = 'TRUE'
        csv_df['WITH_DC'][index] = 'TRUE'
    # print(index, csv_df['WITH_DC'][index])
    

csv_df.to_csv(r'ect_active_plants_units_20200318.csv', quotechar='"', quoting=csv.QUOTE_ALL, index=False)





