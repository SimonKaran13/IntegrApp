import turicreate as tc
import pandas as pd
import os

main_repo_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(main_repo_dir, "data")
combined_data_dir = "merged_data"
database_dir = "database"
stats_dir = "user_stats"
model_dir = "model_dir"

dirs_list = [combined_data_dir, database_dir, stats_dir, model_dir]

def create_all_dirs(dirs_list, data_dir):
    for this_dir in dirs_list:
        if not os.path.exists(os.path.join(data_dir,this_dir)):
            os.mkdir(this_dir)

create_all_dirs(dirs_list, data_dir)

classes_list = ["item", "event", "course", "forum"]

def create_model(data_dir, stats_dir, database_dir, model_dir, combined_data_dir, classes_list):
    for class_name in classes_list:
        stats_file = class_name + "_ratings.csv"
        stat_path = os.path.join(data_dir, stats_dir, stats_file)

        item_file = class_name + "_database.csv"
        database_path = os.path.join(data_dir, database_dir, item_file)

        full_data_file = 'full_' + class_name + '_data.csv'
        full_data_path = os.path.join(data_dir, combined_data_dir, full_data_file)

        stats_df = pd.read_csv(stat_path, sep=";")
        database_df = pd.read_csv(database_path, sep=";")

        merge_key = class_name + "_id"
        full_data_df = database_df.merge(stats_df, how='left', on=merge_key)
        full_data_df.to_csv(full_data_path, index=False, sep=';')

        data_sframe = tc.SFrame.read_csv(full_data_path,
                            delimiter=';',
                            column_type_hints={'rating':int})

        training_data, validation_data = tc.recommender.util.random_split_by_user(data_sframe, 'user_id', merge_key)
        model = tc.recommender.create(training_data, 'user_id', merge_key)

        model_name = class_name + "_recs.model"
        model_path = os.path.join(data_dir, model_dir, model_name)
        model.save(model_path)

create_model(data_dir, stats_dir, database_dir, model_dir, combined_data_dir, classes_list)