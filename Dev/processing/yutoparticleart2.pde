//- - - - - - - - - - - - - - - -パーティクルシステムの配列
ArrayList<Particle> particles;
ArrayList<Particle> particles2;
ArrayList<Particle> particles3;
//- - - - - - - - - - - - - - - -以下時間毎の値
int time1 = 2500;
int time2 = 5000;
int time3 = 7500;
int time4 = 10000;
int time5 = 12500;
int time6 = 15000;
int time7 = 17500;
int time8 = 20000;
int time9 = 22500;
int time10 = 25000;
int time11 = 27500;
int time12 = 30000;
int time13 = 32500;

//- - - - - - - - - - - - - - - -以下初期値
float VEL = 10.0;//最大加速
float ACC = 2.5;//最大加速度
PVector l = new PVector();

//- - - - - - - - - - - - - - - -以下音楽に関するライブラリ
import ddf.minim.*;
Minim minim;
AudioPlayer player;

//- - - - - - - - - - - - - - - -初期設定
void setup(){
  size(980, 730, P3D);
  particles3 = new ArrayList<Particle>();  
  for(int i = 0; i < 2000; i++)
  {
    particles3.add(new Particle());
  }
  minim = new Minim(this);
  player = minim.loadFile("Happy Life (Best No Copyright Music) 30 Min.mp3");
  player.loop();
  smooth(10);
}

//- - - - - - - - - - - - - - - -以下実際に他の関数を呼び出す部分
void draw(){
  background(250,250,250,5);
  //lights();
  //directionalLight(51, 102, 226, 0, -1, 0);
  translate(width/2, height/2,100);
  rotateX(frameCount*0.001);
  rotateY(frameCount*0.001);
  rotateZ(frameCount*0.001);
  //rotate(radians(60));

  for(Particle p: particles3)
  {
   int time = millis();
    if (time > time1)
    {
      p.display4();
      p.update3();
    }
    if (time > time2)
    {
      p.stop();
    }
    if (time > time3)
    {
      p.display4();
      p.update2();
      p.bounceOffWalls();
    }
    if (time > time4)
    {
      p.display4();
      p.update2();
      p.bounceOffWalls();
    }
    if (time > time5)
    {
      p.display3();
      p.update3();
      p.bounceOffWalls();
    }
    if (time > time6)
    {
      p.stop();
    }
    if (time > time7)
    {
      p.update3();
      p.display4();
      p.bounceOffWalls();
    }
    if (time > time8)
    {
      p.update2();
      p.display2();
      p.bounceOffWalls();
    }
    if (time > time9)
    {
      p.update2();
      p.display6();
      p.display2();
    }
    if (time > time10)
    {
      p.update2();
      p.display5();
    }
    if (time > time11)
    {
      p.update2();
      p.display5();
    }
    if (time > time12)
    {
      p.update2();
      p.display5();
    }
    if (time > time13)
    {
      p.update2();
      p.display4();
    }
  }
  
  //saveFrame("frames/####.png");
}

//- - - - - - - - - - - - - - - -パーティクルの中身
class Particle
{
  PVector pos, vel, acc,gravity,loc,sp,force;
  Particle()
  {
    float posSize = noise(800,800,800);
    float posAng1 = random(map(sin(radians(PI)), -100, 100, 0, -100));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float posAng2 = random(map(sin(radians(TWO_PI)), -100, 100, 0, -100));//map(sin(frameCount*0.01), -100, 100, 0, -100)
    float posX = posSize + sin(posAng1) + posAng2;
    float posY = posSize + posAng1 + posAng2; 
    float posZ = posSize + posAng1;
    pos = new PVector(posX, posY, posZ);
    float velSize = random(map(sin(radians(PI)), -100, 100, 0, -100));
    float velAng1 = random(map(sin(radians(PI)), -100, 100, 0, -100));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velAng2 = random(map(sin(radians(PI)), -100, 100, 0, -100));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velX = velSize * velAng1 * velAng1;
    float velY = velSize * velAng1 * velAng2;
    float velZ = velSize * velAng1;
    force = new PVector(12.0, 8.0);
    vel = new PVector(velX,velY,velZ);
    loc = new PVector(random(0, width), random(0, height), random(-100,-700));
    //random(-width, width ), random( -height, height ), random( -100, -700 );
    pos = new PVector(random(0,width), random(0,height), random(-300, -700));
    sp = new PVector();
    acc = new PVector();
    gravity  = new PVector(0.05,0.05,0.05);//0.5,0.5,0.5
    acc = force.mult(ACC);
  }
//- - - - - - - - - - - - - - - -
void update1()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, 100);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
    dir.sub(pos);
    dir.normalize();
    sp.add(dir);
    vel.add(acc);
    vel.limit(VEL*mix);
    pos.add(sp);
    vel.add(gravity);
    pos.add(sp);
}

//- - - - - - - - - - - - - - - -
void update2()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, -100);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
    dir.sub(pos);
    dir.normalize();
    sp.add(dir);
    acc.limit(ACC*mix); //---
    vel.add(acc);
    vel.limit(VEL*mix);
    //pos.add(sp); //--
    //vel.add(gravity);
    pos.add(sp);
    acc.dist(gravity);
}

//- - - - - - - - - - - - - - - -
void update3()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, 100);
    dir.sub(pos);
    dir.normalize();
    acc.set(sp.x,sp.y,sp.z);
    sp.add(dir);
    acc.limit(ACC*mix);
    vel.add(acc);
    vel.limit(VEL*mix);
    pos.add(sp);
    vel.add(gravity);
    pos.add(sp);

}
void update4()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, 100);
    dir.sub(pos);
    dir.normalize();
    acc.set(sp.x,sp.y,sp.z);
    sp.add(dir);
    acc.limit(ACC*mix);
    vel.add(acc);
    vel.limit(VEL*mix);
    pos.add(sp);
    vel.add(gravity);
    pos.add(sp);
}
void update5()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, 100);
   // dir.sub(pos);
    //dir.normalize();
    acc.set(sp.x,sp.y,sp.z);
    sp.add(dir);
    acc.limit(ACC*mix);
    vel.add(acc);
    vel.limit(VEL*mix);
    pos.add(sp);
    vel.add(gravity);
    pos.add(sp);
}



//- - - - - - - - - - - - - - - -
void update()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector( mouseX, mouseY, -500 );
    dir.sub( pos );
    dir.normalize();
    sp.add( dir );
    pos.add( sp );
}

//- - - - - - - - - - - - - - - -//パーティクルの動作遅くする

void stop()
{
    sp.mult(.1);
    sp.add(gravity);
    sp.add(acc);
    vel.add(gravity);
    vel.mult(.1);
    vel.add(acc);
}

//- - - - - - - - - - - - - - - -
void display1()
{
    float mix = player.left.level() * width/50;
    pushMatrix();
    rotateToFace(pos);//240,200,220,5
    translate(-pos.x, pos.y, -pos.z);
    fill(50,200,250,100);
    ellipse(pos.x+mix, pos.y+mix, ACC, ACC);
    translate(pos.x, pos.y, pos.z);
    fill(250,200,200,200);
    ellipse(-pos.x+mix, -pos.y+mix, ACC, ACC);
    stroke(250,0,0,200);
    fill(250,0,0,200);
    ellipse(pos.x, -pos.y+mix, ACC, ACC);
    popMatrix();
}

//- - - - - - - - - - - - - - - -
void display2()
{
    float mix = player.left.level() * width/100;
    pushMatrix();
    rotateToFace(pos);
    translate(-pos.x, pos.y, -pos.z);
    fill(255,0,0,200);
    stroke(255,0,0,250);
    ellipse(pos.x+mix, pos.y, ACC, ACC);
    ellipse(pos.x ,pos.y, ACC, ACC);
    popMatrix();
}

//- - - - - - - - - - - - - - - -
void display3()
{
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    translate(pos.x, pos.y, -pos.z);
    fill(255,0,0,200);
    stroke(255,0,0,250);
    ellipse(pos.x+mix, pos.y,ACC, ACC);
    popMatrix();
}

//- - - - - - - - - - - - - - - -
void display4()
{
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    fill(0,0,0,200);
    stroke(0,0,0,250);
    ellipse(pos.x, -pos.y+mix, ACC, ACC);
    popMatrix();
}

void display5()
{
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    fill(0,0,0,200);
    stroke(0,0,0,250);
    ellipse(pos.x+mix, -pos.y+mix+50, ACC+mix, ACC+mix);
    popMatrix();
}

void display6()
{
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    fill(0,0,0,200);
    stroke(0,0,0,250);
    ellipse(pos.x, -pos.y, ACC, ACC);
    popMatrix();
}



//- - - - - - - - - - - - - - - -
PVector U = new PVector(200,200,200);
void rotateToFace(PVector P)
{
    PVector D = new PVector();
    D.set(l);
    D.sub(P);
    PVector r = U.cross(D);
    r.normalize();
    PVector Backwards = D.cross(U);
    Backwards.normalize();
    PVector rUp = Backwards.cross(r);
    applyMatrix(r.z, r.x, r.y, 100, rUp.x, rUp.y, rUp.z, 0, Backwards.x, Backwards.y, Backwards.z, 0, 0, 0, 0, 1);
 }
 
 void bounceOffWalls() {
    if (pos.x < 0 || pos.x > width) {
      vel.x *= -1;
    }
    if (pos.y < 0 || pos.y > height) {
      vel.y *= -1;
    }
    //画面からはみ出さないように画面内に限定
    pos.x = constrain(pos.x, 0, width);
    pos.y = constrain(pos.y, 0, height);
  }
}
