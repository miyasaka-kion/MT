import os
from huggingface_hub import snapshot_download

# 配置参数
REPO_ID = "Nachtnebel/3036410500-COMP7607-data"  # Hugging Face 仓库 ID
LOCAL_DIR = "data"  # 本地保存路径
TOKEN = None  # 如果需要私有仓库，填写你的 Hugging Face Token（建议用环境变量）

def download_dataset():
    # 确保 data 文件夹存在
    os.makedirs(LOCAL_DIR, exist_ok=True)

    # 下载数据集
    print(f"⏳ 正在从 Hugging Face 下载数据集到 {LOCAL_DIR}...")
    snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        local_dir=LOCAL_DIR,
        token=TOKEN,
    )
    print("✅ 下载完成！")

if __name__ == "__main__":
    download_dataset()
