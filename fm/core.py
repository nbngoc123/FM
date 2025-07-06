import os
import shutil
import datetime

class FM:
    def create_folder(self, path: str) -> None:
        """Tạo một thư mục mới tại đường dẫn được chỉ định.
        
        Args:
            path (str): Đường dẫn của thư mục cần tạo.
            
        Raises:
            OSError: Nếu không thể tạo thư mục do lỗi hệ thống.
        """
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            raise OSError(f"Không thể tạo thư mục {path}: {str(e)}")
    
    def delete_folder(self, path: str) -> None:
        """Xóa một thư mục và toàn bộ nội dung bên trong.
        
        Args:
            path (str): Đường dẫn của thư mục cần xóa.
            
        Raises:
            OSError: Nếu không thể xóa thư mục do lỗi hệ thống.
        """
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
            except OSError as e:
                raise OSError(f"Không thể xóa thư mục {path}: {str(e)}")
        else:
            raise FileNotFoundError(f"Thư mục {path} không tồn tại")
    
    def list_files(self, path: str, extension_filter: str = None) -> list:
        """Liệt kê các tệp trong thư mục được chỉ định, có thể lọc theo phần mở rộng.
        
        Args:
            path (str): Đường dẫn của thư mục cần liệt kê.
            extension_filter (str, optional): Phần mở rộng để lọc tệp (ví dụ: '.txt'). Mặc định là None.
            
        Returns:
            list: Danh sách tên các tệp trong thư mục.
            
        Raises:
            FileNotFoundError: Nếu thư mục không tồn tại.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Thư mục {path} không tồn tại")
        try:
            files = os.listdir(path)
            if extension_filter and isinstance(extension_filter, str):
                return [f for f in files if f.endswith(extension_filter)]
            return files
        except OSError as e:
            raise OSError(f"Không thể liệt kê tệp trong {path}: {str(e)}")
    
    def copy_file(self, src: str, dest: str) -> None:
        """Sao chép một tệp từ nguồn đến đích.
        
        Args:
            src (str): Đường dẫn của tệp nguồn.
            dest (str): Đường dẫn của tệp đích.
            
        Raises:
            FileNotFoundError: Nếu tệp nguồn không tồn tại.
            OSError: Nếu không thể sao chép tệp do lỗi hệ thống.
        """
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Tệp nguồn {src} không tồn tại")
        try:
            shutil.copy(src, dest)
        except OSError as e:
            raise OSError(f"Không thể sao chép tệp từ {src} đến {dest}: {str(e)}")
    
    def move_file(self, src: str, dest: str) -> None:
        """Di chuyển một tệp từ nguồn đến đích.
        
        Args:
            src (str): Đường dẫn của tệp nguồn.
            dest (str): Đường dẫn của tệp đích.
            
        Raises:
            FileNotFoundError: Nếu tệp nguồn không tồn tại.
            OSError: Nếu không thể di chuyển tệp do lỗi hệ thống.
        """
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Tệp nguồn {src} không tồn tại")
        try:
            shutil.move(src, dest)
        except OSError as e:
            raise OSError(f"Không thể di chuyển tệp từ {src} đến {dest}: {str(e)}")
    
    def rename(self, old_path: str, new_path: str) -> None:
        """Đổi tên một tệp hoặc thư mục.
        
        Args:
            old_path (str): Đường dẫn hiện tại của tệp/thư mục.
            new_path (str): Đường dẫn mới của tệp/thư mục.
            
        Raises:
            FileNotFoundError: Nếu đường dẫn hiện tại không tồn tại.
            OSError: Nếu không thể đổi tên do lỗi hệ thống.
        """
        if not os.path.exists(old_path):
            raise FileNotFoundError(f"Đường dẫn {old_path} không tồn tại")
        try:
            os.rename(old_path, new_path)
        except OSError as e:
            raise OSError(f"Không thể đổi tên {old_path} thành {new_path}: {str(e)}")
    
    def exists(self, path: str) -> bool:
        """Kiểm tra xem một tệp hoặc thư mục có tồn tại hay không.
        
        Args:
            path (str): Đường dẫn cần kiểm tra.
            
        Returns:
            bool: True nếu đường dẫn tồn tại, False nếu không.
        """
        return os.path.exists(path)
    
    def get_file_info(self, path: str) -> dict:
        """Lấy thông tin chi tiết về một tệp.
        
        Args:
            path (str): Đường dẫn của tệp cần kiểm tra.
            
        Returns:
            dict: Thông tin về tệp bao gồm kích thước, ngày tạo, ngày sửa đổi.
            
        Raises:
            FileNotFoundError: Nếu tệp không tồn tại.
        """
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Tệp {path} không tồn tại")
        stats = os.stat(path)
        return {
            "size": stats.st_size,  # Kích thước tệp tính bằng byte
            "created": datetime.datetime.fromtimestamp(stats.st_ctime).isoformat(),
            "modified": datetime.datetime.fromtimestamp(stats.st_mtime).isoformat()
        }
