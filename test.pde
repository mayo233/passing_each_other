import gab.opencv.*;

PImage given_img;    //初期地図
PImage change_img = createImage(width, height, RGB);
PImage change_img_1 = createImage(width, height, RGB);

//変数宣言 エージェント
int[] agent1 =new int[2];  //agent1はx,y座標を持っている
int[] agent2 =new int[2];  //agent2はx,y座標を持っている
int agent_x =10;    //agentのx座標の大きさ
int agent_y =10;   //agentのy座標の大きさ
int agent_num=100;  //空きスペースに入るエージェント番号
int stop_time; //エージェントの停止時間
int count_collision;  //衝突回数
int space_enter_t=0;    //ブロックを壊し始める時間
int step=0;  //ステップ数を計測
int count =0;
int B=66; //ブロックの個数
int break_block_num=0;  //改変するブロック番号

//ブロックの変数宣言
int[] blf =new int[B] ; //ブロックの数
int blw =10;    //ブロックの横幅
int blh =10;  //ブロックの縦幅
int break_block=0;  //破壊するブロック

//判定を行う変数宣言
boolean collision ; //エージェント同士が衝突しそうになったか判定する変数
boolean space ; //空きスペースに入るのか判定する変数
boolean once =false;    //どっちのエージェントが空きスペースに入るか判定する
boolean stop =false;  //エージェントを停止させるか判定する
boolean temp =false;  //エージェントを停止させるか判定する
boolean block_num=false;  //エージェントを停止させるか判定する


//ブロックとエージェントの当たり判定
int blockHitCheck() {

  if (agent_num ==0 || agent_num ==1) {
    if (block_num ==false) {
      break_block =agent2[0]/12;
      block_num=true;
    }
  }
  return break_block;

  //if (break_block !=0 ) {
  //  //blf[break_block] =0;
  //  //println(break_block);

  //}
}

//エージェント１ or 2のどっちが空きスペースに入るか判定する関数
int agent_or_space () {

  if (((agent1[0]) -((agent1[0]/12) *12) + blw/2) < ((agent2[0] ) - ((agent2[0]/12) *12) + blw/2 )) {

    return 0;
  } else {
    //println((agent1[0]) -((agent1[0]/12) *12) + blw/2);
    //println(agent1[0]);
    //println("---------");
    //println((agent2[0]) -((agent2[0]/12) *12) + blw/2);
    //println(agent2[0]);
    //delay(4000);
    return 1;
  }
}

void agent_move() {

  //エージェント番号を可視化
  textSize(40);
  text("1", agent1[0], agent1[1]+20, 60, 600);  //エージェント1
  text("2", agent2[0], agent2[1]+20, 60, 600);  //エージェント2
  //text(millis()/1000, 450, 40);  //時間計測

  if (temp ==false) {
    agent1[0] +=1;
    if (agent2[0] -agent1[0]  <=13) {
      if (once ==false) {
        agent_num=agent_or_space();
        break_block_num=blockHitCheck();
        once =true;
      }

      agent2[0] +=1;
    }
    if (agent1[0] ==512) {
      temp=true;
    }
  } else {
    agent2[0] -=1;
    //println(break_block_num);
    //rect((break_block_num%B) *(blw+2), 110, blw, blh);
    //color c =get((break_block_num%B) *(blw+2), 110,10,10);
    //image(change_img, (break_block_num%B) *(blw+2), 80,10,10);
    //change_img=given_img;

    //println(get((break_block_num%B) *(blw+2), 110,10,10));


    if (agent2[0] ==-10) {
      //改変した地図を作ってsaveする ここで
      //画面を画像にコピー
      //image(change_img, (break_block_num%B) *(blw+2), 110, 10, 10);
      //change_img =given_img;
      //change.save("");
      given_img.set((break_block_num%B) *(blw+2), 80, change_img);
      given_img.save("change_map.png");

      exit();    //プログラム終了
    }
  }
  ellipse(agent1[0], agent1[1], agent_x, agent_y);  //エージェント1
  ellipse(agent2[0], agent2[1], agent_x, agent_y);  //エージェント2
  //step+=1;
  //println(step);
}

void setup() {
  size(500, 500);
  given_img=loadImage("given_map.png");
  change_img=loadImage("black_block.png");

  //初期設定
  size( 500, 500);
  agent1[0] =100; //agent1のx座標の初期位置
  agent1[1] =100; //agent1のy座標の初期位置
  agent2[0] =400; //agent2のx座標の初期位置
  agent2[1] =100; //agent2のy座標の初期位置
  count_collision =0; //衝突回数
  stop_time=0;
  collision =false; //衝突していない
  space =false; //空きスペースに入っていない
  step=0; //ステップ数を計測
}

void draw() {
  image(given_img, 0, 0);    //初期地図を表示
  agent_move();  //エージェントを動かす
}
