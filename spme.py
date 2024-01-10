import os

def split_file(file_path, num_splits):
    # 获取文件大小
    file_size = os.path.getsize(file_path)
    
    # 计算每个拆分文件的大小
    split_size = file_size // num_splits
    
    # 打开原始文件
    with open(file_path, 'rb') as f:
        # 逐个拆分文件
        for i in range(num_splits):
            # 生成拆分文件名
            split_file_name = f'{file_path}.split{i}'
            
            # 打开拆分文件
            with open(split_file_name, 'wb') as split_file:
                # 读取拆分文件大小的数据
                data = f.read(split_size)
                
                # 写入拆分文件
                split_file.write(data)
    
    print(f'文件拆分完成！共拆分为 {num_splits} 个文件。')

def merge_files(file_path):
    # 获取文件所在目录和文件名
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    
    # 获取拆分文件列表
    split_files = [f for f in os.listdir(file_dir) if f.startswith(file_name) and f != file_name]
    
    # 按文件名排序
    split_files.sort()
    
    # 打开合并后的文件
    with open(file_path, 'wb') as merged_file:
        # 逐个合并文件
        for split_file in split_files:
            # 打开拆分文件
            with open(os.path.join(file_dir, split_file), 'rb') as f:
                # 读取拆分文件数据
                data = f.read()
                
                # 写入合并后的文件
                merged_file.write(data)
    
    print('文件合并完成！')

# 测试拆分和合并文件
file_path = './epoch100_model.pth'
num_splits = 20

split_file(file_path, num_splits)
# merge_files(file_path)
