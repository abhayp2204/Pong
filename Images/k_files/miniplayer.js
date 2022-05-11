(function(g){var window=this;'use strict';var o6=function(a){g.V.call(this,{D:"div",K:"ytp-miniplayer-ui"});this.yf=!1;this.player=a;this.N(a,"minimized",this.gg);this.N(a,"onStateChange",this.UE)},p6=function(a){g.iN.call(this,a);
this.i=new o6(this.player);this.i.hide();g.ZM(this.player,this.i.element,4);a.Be()&&(this.load(),g.N(a.getRootNode(),"ytp-player-minimized",!0))};
g.w(o6,g.V);g.k=o6.prototype;
g.k.iD=function(){this.tooltip=new g.EQ(this.player,this);g.I(this,this.tooltip);g.ZM(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.pc=new g.dO(this.player);g.I(this,this.pc);this.rg=new g.V({D:"div",K:"ytp-miniplayer-scrim"});g.I(this,this.rg);this.rg.Ba(this.element);this.N(this.rg.element,"click",this.bz);var a=new g.V({D:"button",Ea:["ytp-miniplayer-close-button","ytp-button"],U:{"aria-label":"Close"},S:[g.iL()]});g.I(this,a);a.Ba(this.rg.element);this.N(a.element,"click",this.wi);
a=new g.M1(this.player,this);g.I(this,a);a.Ba(this.rg.element);this.Vo=new g.V({D:"div",K:"ytp-miniplayer-controls"});g.I(this,this.Vo);this.Vo.Ba(this.rg.element);this.N(this.Vo.element,"click",this.bz);var b=new g.V({D:"div",K:"ytp-miniplayer-button-container"});g.I(this,b);b.Ba(this.Vo.element);a=new g.V({D:"div",K:"ytp-miniplayer-play-button-container"});g.I(this,a);a.Ba(this.Vo.element);var c=new g.V({D:"div",K:"ytp-miniplayer-button-container"});g.I(this,c);c.Ba(this.Vo.element);this.nL=new g.BP(this.player,
this,!1);g.I(this,this.nL);this.nL.Ba(b.element);b=new g.yP(this.player,this);g.I(this,b);b.Ba(a.element);this.nextButton=new g.BP(this.player,this,!0);g.I(this,this.nextButton);this.nextButton.Ba(c.element);this.xg=new g.rQ(this.player,this);g.I(this,this.xg);this.xg.Ba(this.rg.element);this.Ic=new g.GP(this.player,this);g.I(this,this.Ic);g.ZM(this.player,this.Ic.element,4);this.Oy=new g.V({D:"div",K:"ytp-miniplayer-buttons"});g.I(this,this.Oy);g.ZM(this.player,this.Oy.element,4);a=new g.V({D:"button",
Ea:["ytp-miniplayer-close-button","ytp-button"],U:{"aria-label":"Close"},S:[g.iL()]});g.I(this,a);a.Ba(this.Oy.element);this.N(a.element,"click",this.wi);a=new g.V({D:"button",Ea:["ytp-miniplayer-replay-button","ytp-button"],U:{"aria-label":"Close"},S:[g.nL()]});g.I(this,a);a.Ba(this.Oy.element);this.N(a.element,"click",this.eU);this.N(this.player,"presentingplayerstatechange",this.Hc);this.N(this.player,"appresize",this.tb);this.N(this.player,"fullscreentoggled",this.tb);this.tb()};
g.k.show=function(){this.yd=new g.Cq(this.Np,null,this);this.yd.start();this.yf||(this.iD(),this.yf=!0);0!==this.player.getPlayerState()&&g.V.prototype.show.call(this);this.Ic.show();this.player.unloadModule("annotations_module")};
g.k.hide=function(){this.yd&&(this.yd.dispose(),this.yd=void 0);g.V.prototype.hide.call(this);this.player.Be()||(this.yf&&this.Ic.hide(),this.player.loadModule("annotations_module"))};
g.k.va=function(){this.yd&&(this.yd.dispose(),this.yd=void 0);g.V.prototype.va.call(this)};
g.k.wi=function(){this.player.stopVideo();this.player.Na("onCloseMiniplayer")};
g.k.eU=function(){this.player.playVideo()};
g.k.bz=function(a){if(a.target===this.rg.element||a.target===this.Vo.element)g.T(this.player.T().experiments,"kevlar_miniplayer_play_pause_on_scrim")?g.lK(this.player.ub())?this.player.pauseVideo():this.player.playVideo():this.player.Na("onExpandMiniplayer")};
g.k.gg=function(){g.N(this.player.getRootNode(),"ytp-player-minimized",this.player.Be())};
g.k.jd=function(){this.Ic.Rb();this.xg.Rb()};
g.k.Np=function(){this.jd();this.yd&&this.yd.start()};
g.k.Hc=function(a){g.U(a.state,32)&&this.tooltip.hide()};
g.k.tb=function(){g.RP(this.Ic,0,this.player.Za().getPlayerSize().width,!1);g.IP(this.Ic)};
g.k.UE=function(a){this.player.Be()&&(0===a?this.hide():this.show())};
g.k.fc=function(){return this.tooltip};
g.k.Le=function(){return!1};
g.k.jf=function(){return!1};
g.k.di=function(){return!1};
g.k.Lz=function(){};
g.k.Mm=function(){};
g.k.qr=function(){};
g.k.cn=function(){return null};
g.k.dj=function(){return new g.ql(0,0,0,0)};
g.k.handleGlobalKeyDown=function(){return!1};
g.k.handleGlobalKeyUp=function(){return!1};
g.k.Up=function(a,b,c,d,e){var f=0,h=d=0,l=g.Ql(a);if(b){c=g.Mq(b,"ytp-prev-button")||g.Mq(b,"ytp-next-button");var m=g.Mq(b,"ytp-play-button"),n=g.Mq(b,"ytp-miniplayer-expand-watch-page-button");c?f=h=12:m?(b=g.Ol(b,this.element),h=b.x,f=b.y-12):n&&(h=g.Mq(b,"ytp-miniplayer-button-top-left"),f=g.Ol(b,this.element),b=g.Ql(b),h?(h=8,f=f.y+40):(h=f.x-l.width+b.width,f=f.y-20))}else h=c-l.width/2,d=25+(e||0);b=this.player.Za().getPlayerSize().width;e=f+(e||0);l=g.Pf(h,0,b-l.width);e?(a.style.top=e+"px",
a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.k.showControls=function(){};
g.k.Qk=function(){};
g.k.pk=function(){return!1};g.w(p6,g.iN);p6.prototype.create=function(){};
p6.prototype.Hi=function(){return!1};
p6.prototype.load=function(){this.player.hideControls();this.i.show()};
p6.prototype.unload=function(){this.player.showControls();this.i.hide()};g.tN.miniplayer=p6;})(_yt_player);
