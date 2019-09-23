import os

class Config:

    user = "gokul"
    lang = "hindi"

    image_size = [512, 512, 3]
    geometry = "QUAD" # ["RBOX", "QUAD"]
    label_method = "single" # ["single", "multiple"]

    max_m_train = 10000
    data_dir = "/home/{}/data-split/{}".format(user, lang)
    train_data_dir = os.path.join(data_dir, 'train')
    dev_data_dir = os.path.join(data_dir, 'dev')
    test_data_dir = os.path.join(data_dir, 'test')

    lambda_geometry = 1
    epochs = 5
    learning_rate = 0.01
    mini_batch_size = 2