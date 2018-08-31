diem = int(input("Nhập điểm của bạn: "))
if diem >= 8:
    xephang = 'Giỏi'
elif diem > 6.5:
    xephang = 'Khá'
elif diem > 5:
    xephang = 'Trung Bình'
else:
    xephang = 'Yếu'
print("Xếp hạng học lực của bạn là: ", xephang)