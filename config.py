## dataset configuartion
batch_size = 64
out_level = "character"
image_dir = ""
image_size = (-1, 128)

## training configuration
max_epoch = 100
learning_rate = 5e-5
checkpoint_path = "saved_models"
start_from = None
warmup = 10000

## model configuration
dropout = 0.5
num_layers = 4
d_model = 256
dff = 512
heads = 8
beam_size = 2

## objective function configuration
smoothing = 0.3

## configure for debug only
debug = True
save_per_iter = 100
tmp_checkpoint_path = "tmp_saved_models"