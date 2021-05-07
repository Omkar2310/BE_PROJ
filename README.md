# BE_PROJ
PARTIAL FACE RECOGNITION USING DEEP LEARNING

Steps to run the current project

1) Create a dataset folder with individual_name -> pics(without mask)
2) we have generate_databasepy file run it it converts dataset to masked dataset.
3)then get dataset_with_mask.zip file upload it to colab on train.ipynb
4) run all commands then at one point after

learn.export() line we get a export.pkl file it is our model for corresponding dataset

5)Now keep export file in same directory as you are now
learn = load_learner(“.”)

classNames = ['angela_markel','anushka_sharma','donald_trump','manisha','narendra_modi','omkar',"salman_khan",'shushant_singh_rajput',"valdimir_putin"]

these are dataset_ids for now


so learn now has our model testing

img = open_image('test_image.jpeg')
//(image.jpg is any random image.)
img.show(figsize=(3, 3))
pred_class,preds_idx,outputs = learn.predict(img)
pred_class //this gives tensor

classNames[preds_idx]	//given name like omkar,donald trump ...etc

