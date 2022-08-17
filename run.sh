nohup python main.py \
--bert_dir="../model_hub/roberta_base_model/" \
--data_dir="./data/custom/" \
--data_name="custom" \
--log_dir="./logs/" \
--output_dir="./checkpoints/" \
--num_tags=54 \
--seed=123 \
--gpu_ids="1" \
--max_seq_len=256 \
--lr=3e-5 \
--other_lr=3e-4 \
--train_batch_size=64 \
--train_epochs=3 \
--eval_batch_size=16 \
--do_train \
--do_test \
--do_predict  >logs/epoch3_entity_0816.log 2>&1 &

