import pandas as pd
import csv

csv_df = pd.read_csv('ect_ECTT0007_plant.csv')

csv_df = csv_df.drop(columns=['time_zone', 'maintainer'])

csv_df = csv_df[[
        'plant_name',
        'plant_no',
        'plant_alias',
        'capacity',
        'plant_address',
        'plant_address_no',
        'longitude',
        'latitude',
        'city',
        'county',
        'holding',
        'spv',
        'om',
        'epc',
        'agent',
        'owner',
        'on_grid_date',
        'fee_rate',
        'active',
       ]]

csv_main_df = csv_df

# ======================================================================
# ======================================================================
# ======================================================================

csv_df = pd.read_csv('ect_active_plants_20200303.csv')

csv_df = csv_df.drop(columns=[
                            'project_status',
                            'maintainer',
                            'updated_at',
                            ])

csv_df = csv_df[[
        'plant_name',
        'plant_no',
        'plant_alias',
        'capacity',
        'plant_address',
        'plant_address_no',
        'longitude',
        'latitude',
        'city',
        'county',
        'holding',
        'spv',
        'om',
        'epc',
        'agent',
        'on_grid_date',
        'fee_rate',
        'active',
        ]]

csv_main_df = csv_main_df.append(csv_df, ignore_index=True)


# ======================================================================
# ======================================================================
# ======================================================================

csv_main_df = csv_main_df[[
        'plant_name',
        'plant_no',
        'plant_alias',
        'capacity',
        'plant_address',
        'plant_address_no',
        'longitude',
        'latitude',
        'city',
        'county',
        'holding',
        'spv',
        'om',
        'epc',
        'agent',
        'owner',
        'on_grid_date',
        'fee_rate',
        'active',
       ]]

csv_main_df.to_csv(r'ect_active_plants_20200318.csv', quotechar='"', quoting=csv.QUOTE_ALL, index=False)

csv_df = pd.read_csv('ect_active_plants_20200318.csv')
csv_df = csv_df.fillna('NULL')
csv_df.to_csv(r'ect_active_plants_20200318-new.csv', quotechar='"', quoting=csv.QUOTE_ALL, index=False)