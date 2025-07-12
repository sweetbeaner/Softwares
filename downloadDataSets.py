import os
import sys
import json

# 自动安装 modelscope（如未安装）
try:
    from modelscope.msdatasets import MsDataset
except ImportError:
    print("modelscope 未安装，正在尝试安装...")
    os.system(f"{sys.executable} -m pip install modelscope")
    from modelscope.msdatasets import MsDataset

def download_aerospace_subset(output_file='aerospace_subset.jsonl'):
    print("🔍 开始加载数据集 BAAI/IndustryCorpus2...")
    dataset = MsDataset.load('BAAI/IndustryCorpus2', split='train', namespace='BAAI')
    print(f"✅ 数据集加载完成，共 {len(dataset)} 条记录")

    print("🔍 筛选 domain 为 'aerospace' 的子集...")
    aerospace_data = [item for item in dataset if item.get('domain', '').lower() == 'aerospace']
    print(f"✅ 找到 {len(aerospace_data)} 条 aerospace 数据")

    print(f"💾 正在保存到文件：{output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in aerospace_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

    print(f"🎉 保存成功，共 {len(aerospace_data)} 条记录写入 {output_file}")

if __name__ == '__main__':
    download_aerospace_subset()
