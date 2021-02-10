import ddf.minim.*;
Minim minim;
AudioPlayer player;

import ddf.minim.analysis.*;
AudioInput in;
FFT fft;

import processing.video.*;
import jp.nyatla.nyar4psg.*;
import processing.core.PImage.*;
Capture cam;
MultiMarker nya;
PImage img;


final boolean isSave = true; // save as png
final int N = 5000; // arc number
final int lineSize = 5; // arc line size
final float radiusMin = 10; 
final float radiusMax = 300;
float arcRange = radians(random(100));


String getPngName()
{
  return "arc_"
    + "_N_" + N
    + "_lineSize_" + lineSize
    + "_radiusMin_" + radiusMin
    + "_radiusMax_" + radiusMax
    + "_arcRange_" + arcRange
    + ".png";
}



void setup(){
     //tint(0,0,0,10);
     background(0,0,0,10);
    size(930, 770);
    strokeWeight(lineSize);
    strokeCap(RECT);
    noFill();

    for (int i = 0; i < N; ++i) 
    {
        stroke(random(1,255));
        //drawArc();
    }
    
    if (isSave)
    {
      save(getPngName()); // save as png
    }
    
  
  minim = new Minim(this);
  player = minim.loadFile("HIRAHIRA.mp3");
  player.loop();
   fft = new FFT(player.bufferSize(), player.sampleRate());
}

void draw(){
    float beatR = player.left.level() * width/10;
    float beatL = player.right.level() * width/10;
    float mix = player.mix.level();
    float x1 = width / 2;
    float y = height / 2;
    float r = random(radiusMin, radiusMax);
    float size = r * 2;
    float radian1 = random(0, 2 * PI);
    float radian2 = radian1 + arcRange;
    float x = 0.68;
    float j = 0.5;
    int t = 20;
    //img.get(100,100,100,100);
    translate(30,5);
    scale(x);
    pushMatrix();
    noFill();
    
//strokeWeight(5);
//fill(30);//fill(51,204,204,50);
stroke(random(50),204,255,50);
strokeWeight(lineSize/2);
strokeCap(RECT);
noFill();
arc(0, 0, size, size, radian1*beatR, radian2);
stroke(20,random(200),100,50);
arc(0,0, size, size, radian1/2, radian2/2);
stroke(40);
strokeWeight(5);
rect(0,0,269.23-t,269.23-t);
//image(img, 0, 0,269.23-t,269.23-t);
rect(269.25,0,161.55-t,161.55-t);
strokeWeight(lineSize/5);
stroke(40,100,90,80);
arc(269.25,0, size, size, radian1, radian2);
//arc(269.25,0, size, size, radian1, radian2);
//image(img,269.25,0,161.55-t,161.55-t);
//fill(0);
rect(0,269.25,430.77-t,430.77-t);
//arc(0,269.25, size, size, radian1, radian2);
//image(img,0,269.25,430.77-t,430.77-t);
//fill(0);
rect(323.08,161.55,107.7-t,107.7-t);
//arc(323.08,161.55, size, size, radian1, radian2);
//image(img,323.08,161.55,107.7-t,107.7-t);
translate(269.25,161.55);
rect(0,0,53.85-t,53.85-t);
stroke(255);
arc(0,0, size, size, radian1, radian2);
//arc(0,0, size, size, radian1, radian2);
//image(img,0,0,53.85-t,53.85-t);
translate(0,53.85);
//fill(50);//fill(255,40,40,40);
rect(0,0,53.85-t,53.85-t);
//arc(0,0, size, size, radian1, radian2);
//image(img,0,0,53.85-t,53.85-t);
stroke(40);
//fill(30);
//fill(51,204,204,50);
translate(165,-215);
rect(165,430.77,269.23-t,269.23-t);
strokeWeight(lineSize/3);
strokeCap(RECT);
noFill();
//stroke(random(200),50,80,30);
arc(165,430.77, size, size, radian1, radian2);
stroke(random(255),50,30,30);
arc(165,430.77, size, size, radian1, radian2);
//image(img,165,430.77,269.23-t,269.23-t);
rect(0,430.77,161.55-t,161.55-t);
//image(img,0,430.77,161.55-t,161.55-t);
//fill(0);
rect(0,0,430.77-t,430.77-t);
//image(img,0,0,430.77-t,430.77-t);
//fill(0);
rect(0,592.3,107.7-t,107.7-t);
//image(img,0,592.3,107.7-t,107.7-t);
translate(269.25,161.55);
rect(-160,430.77,53.85-t,53.85-t);
stroke(50,50,255,30);
arc(-160,430.77, size, size, radian1, radian2);
//image(img,-160,430.77,53.85-t,53.85-t);
translate(0,53.85);
//fill(255,255,153,50);
//fill(50);//fill(255,40,40,40);
rect(-160,430.77,53.85-t,53.85-t);
//image(img,-160,430.77,53.85-t,53.85-t);

//fill(30);
//fill(51,204,204,20);
translate(160,215);
rect(165,430.77,269.23-t,269.23-t);
//image(img,165,430.77,269.23-t,269.23-t);
rect(0,430.77,161.55-t,161.55-t);
//image(img,0,430.77,161.55-t,161.55-t);
//fill(0);
rect(0,0,430.77-t,430.77-t);
strokeWeight(lineSize/2);
strokeCap(RECT);
noFill();
arc(0,0, size, size, radian1, radian2);
//image(img,0,0,430.77-t,430.77-t);
//fill(100);
rect(0,592.3,107.7-t,107.7-t);
//image(img,0,592.3,107.7-t,107.7-t);
translate(269.25,161.55);
rect(-160,430.77,53.85-t,53.85-t);
//image(img,-160,430.77,53.85-t,53.85-t);
translate(0,53.85);
//fill(255,150,50,20);
//fill(122, 176, 0);
rect(-160,430.77,53.85-t,53.85-t);
stroke(250,200,100,50);
arc(-160,430.77, size, size, radian1, radian2);
//image(img,-160,430.77,53.85-t,53.85-t);

//fill(30);
//fill(51,204,204,50);
translate(-290,50);
rotate(radians(90));
//fill(40);
rect(165,430.77,269.23-t,269.23-t);
//image(img,165,430.77,269.23-t,269.23-t);
rect(0,430.77,161.55-t,161.55-t);
//image(img,0,430.77,161.55-t,161.55-t);
//fill(0);
rect(0,0,430.77-t,430.77-t);
//image(img,0,0,430.77-t,430.77-t);
//fill(100);
rect(0,592.3,107.7-t,107.7-t);
//image(img,0,592.3,107.7-t,107.7-t);
translate(269.25,161.55);
rect(-160,430.77,53.85-t,53.85-t);
strokeWeight(lineSize/3);
strokeCap(RECT);
noFill();
stroke(100,100,250,50);
arc(-160,430.77, size, size, radian1, radian2);
stroke(0, 175, 255,50);
arc(-160,430.77, size, size, radian1, radian2);
//image(img,-160,430.77,53.85-t,53.85-t);
translate(0,53.85);
//fill(50);//fill(255,255,153,50);
rect(-160,430.77,53.85-t,53.85-t);
//image(img,-160,430.77,53.85-t,53.85-t);

stroke(255,100,random(50),50);
//fill(30);
translate(5,-700);
//fill(51,204,204,50);
translate(-290,50);
rotate(radians(90));
rect(165,430.77,269.23-t,269.23-t);
strokeWeight(lineSize/3);
strokeCap(RECT);
noFill();
arc(165,430.77, size, size, radian1, radian2);
stroke(255,100,50,50);
arc(0,0, size, size, radian1, radian2);
//image(img,165,430.77,269.23-t,269.23-t);
//fill(50);
rect(0,430.77,161.55-t,161.55-t);
//image(img,0,430.77,161.55-t,161.55-t);
//fill(51,153,102,50);
//fill(100);//fill(255,40,40,40);
rect(0,592.3,107.7-t,107.7-t);
stroke(255,60,50,50);
arc(0,592.3, size, size, radian1, radian2);
//image(img,0,592.3,107.7-t,107.7-t);
translate(269.25,161.55);
rect(-160,430.77,53.85-t,53.85-t);
//image(img,-160,430.77,53.85-t,53.85-t);
translate(0,53.85);
//fill(255,255,153,50);
//fill(122, 176, 0,50);
rect(-160,430.77,53.85-t,53.85-t);
arc(-160,430.77, size/2, size/2, radian1, radian2);
//image(img,-160,430.77,53.85-t,53.85-t);
popMatrix();
scale(x);
stroke(40);

//int c =  img.get(width,height);//stroke(random(c));
scale(0.68);
//strokeWeight(5);
//arc(x1, y, size, size, radian1, radian2);
//arc(x1, y, size, size, radian1, radian2);
//scale(0.68);
//strokeWeight(5);
//strokeWeight(3);




}

/*
void drawArc()
{
    float x = width / 2;
    float y = height / 2;
    float r = random(radiusMin, radiusMax);
    float size = r * 2;
    float radian1 = random(0, 2 * PI);
    float radian2 = radian1 + arcRange;
    arc(x, y, size, size, radian1, radian2);
}
*/


/*
fft.forward(player.mix);
      for (int j = 0; j < fft.specSize(); j++)
  {
   float m = map(j, 1, fft.specSize(), 1, width);
   
   arc(x, y, size, size, radian1, radian2);
  }
  
point(screenWidth/2,screenHeight/2);
AR

if (cam.available() !=true) {
      return;
  }
  cam.read();
  //cam.loadPixels();
  nya.detect(cam);
  //background(0);
  nya.drawBackground(cam);//frustumを考慮した背景描画
  if((!nya.isExist(0))){
    return;
  }
  nya.beginTransform(0);

nya.endTransform();

   println(MultiMarker.VERSION);
  cam=new Capture(this,640,480);
  nya=new MultiMarker(this,width,height,"../../data/camera_para.dat",NyAR4PsgConfig.CONFIG_PSG);
  nya.addNyIdMarker(0,100);
  cam.start();
  
       img = loadImage("code.jpg");
     img = img.get( 50,50, width, height );
     img.loadPixels();
  */
