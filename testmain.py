# import torch
# print(torch.cuda.is_available())
# print(torch.cuda.device_count())
# print(torch.cuda.get_device_name())
import torch
model = torch.hub.load('pytorch/vision', 'vit_b_32', pretrained=True)

