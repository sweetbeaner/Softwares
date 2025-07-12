import wandb
import json

history_file = "wandb/run-20250708-101005-lxkow75j/wandb-history.jsonl"

# 读取 history 文件
with open(history_file, "r") as f:
    lines = f.readlines()

# 启动新的 run
wandb.init(project="your_project", name="reupload-partial-history")

# 只每隔100步上传一条
for i, line in enumerate(lines):
    if i % 100 == 0:
        data = json.loads(line)
        wandb.log(data, step=data.get("_step", i))

wandb.finish()
