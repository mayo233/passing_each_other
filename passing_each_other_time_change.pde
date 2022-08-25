//変数宣言 エージェント
int[] agent1 =new int[2];  //agent1はx,y座標を持っている
int[] agent2 =new int[2];  //agent2はx,y座標を持っている
int agent_x =10;    //agentのx座標の大きさ
int agent_y =10;   //agentのy座標の大きさ
int agent_num=0;  //空きスペースに入るエージェント番号
int stop_time; //エージェントの停止時間
int count_collision;  //衝突回数
int space_enter_t=0;    //ブロックを壊し始める時間
int step=0; //ステップ数

//ブロックの変数宣言
int[] blf =new int[50] ; //ブロックの数
int blw =10;    //ブロックの横幅
int blh =10;  //ブロックの縦幅
int break_block=0;  //破壊するブロック

//判定を行う変数宣言
boolean collision ; //エージェント同士が衝突しそうになったか判定する変数
boolean space ; //空きスペースに入るのか判定する変数
boolean once =false;    //どっちのエージェントが空きスペースに入るか判定する
boolean stop =false;  //エージェントを停止させるか判定する


void blockDisp() {
  for (int i=0; i<blf.length; i++) {
    blf[i] =1;  //0:ブロック非表示 1:ブロック表示
  }
  for (int i=blf.length-1; i >=0; i--) {

    if (blf[i] ==1) {
      fill(255, 255, 255);
      //blockHitCheck();
      rect((i%50) *(blw+2), 110, blw, blh);    //下のブロック
      if (i==33) {
        continue;
      }

      rect((i%50) *(blw+2), 80, blw, blh);    //上のブロック
    }
  }
}

//ブロックとエージェントの当たり判定
void blockHitCheck() {

  if (agent2[1] !=100) {
    break_block =agent2[0]/12;
  } else if (agent1[1] !=100) {
    break_block =agent1[0]/12;
  }

  if (break_block !=0 ) {
    blf[break_block] =0;
    //println(break_block);
  }
}

//エージェント１ or 2のどっちが空きスペースに入るか判定する関数
int agent_or_space () {

  if (((agent1[0]) -((agent1[0]/12) *12) + blw/2) < ((agent2[0] ) - ((agent2[0]/12) *12) + blw/2 )) {

    return 0;
  } else {
    println((agent1[0]) -((agent1[0]/12) *12) + blw/2);
    println(agent1[0]);
    println("---------");
    println((agent2[0]) -((agent2[0]/12) *12) + blw/2);
    println(agent2[0]);
    //delay(4000);
    return 1;
  }
}

void agent_move() {

  //エージェント番号を可視化  14s
  textSize(40);
  text("1", agent1[0], agent1[1]+20, 60, 600);  //エージェント1
  text("2", agent2[0], agent2[1]+20, 60, 600);  //エージェント2
  //text(millis()/1000, 450, 40);  //時間計測

  //160 衝突 バックを入れる？？  123 うまくいった  128　微妙?
  if (stop_time  >=300 && collision ==false) {
    if (agent2[0] !=-10) {
      agent2[0] -=1;
    }
    if (agent2[0] ==-10) {
      exit();
    }
  }

  ellipse(agent1[0], agent1[1], agent_x, agent_y);  //エージェント1
  ellipse(agent2[0], agent2[1], agent_x, agent_y);  //エージェント2

  //エージェント１と2が衝突しそうになった時
  if (agent2[0] - agent1[0] <13  ) {

    if (once ==false) {
      agent_num = agent_or_space();
      once =true;
    }

    if (count_collision ==0) {
      collision =true;
    }
  }

  //衝突しそうにない時
  if (collision ==false ) {
    if (agent1[0] !=512) {
      agent1[0] +=1;  //エージェント１は左からくる
    }
  } else if (collision ==true) {
    if (space ==false) {

      //衝突しそうになっていて空きスペースに入っていない時
      if (agent_num ==0) {
        agent1[1] -=1;
        agent2[0] -=1;
      } else {
        agent2[1] -=1;
        agent1[0] +=1;
      }
      if (agent1[1] ==85 || agent2[1] ==85) {
        space =true;
        if (agent_num ==0) {
          agent1[1] -=1;
          agent2[0] -=1;
        } else {
          agent1[0] +=1;
          agent2[1] -=1;
        }
      }
    } else if (space ==true) {

      //ブロックを壊した時
      if (agent_num ==0) {
        agent1[1] +=1;
        agent2[0] -=1;
      } else {
        agent2[1] +=1;
        agent1[0] +=1;
      }
      if (agent1[1] ==100 && agent2[1] ==100) {
        collision =false;
        space =false;
        count_collision++;
      }
    }
  }
  stop_time+=1;
  step+=1;
  println(step);
}

void setup() {
  //初期設定
  size(500, 500);
  agent1[0] =100; //agent1のx座標の初期位置
  agent1[1] =100; //agent1のy座標の初期位置
  agent2[0] =400; //agent2のx座標の初期位置
  agent2[1] =100; //agent2のy座標の初期位置
  count_collision =0; //衝突回数
  stop_time=0;
  collision =false; //衝突していない
  space =false; //空きスペースに入っていない
}

void draw() {
  background(0); //背景を黒にする
  blockDisp();    //ブロックの表示
  agent_move();  //エージェントを動かす
}
