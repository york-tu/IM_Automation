package tw.com.pardise_soft;

import org.sikuli.script.*;
import py4j.GatewayServer;

public class SikuliApi {
	public static GatewayServer server;
	public Screen screen() {
		Screen s = new Screen();
		return s;
	}

	public Pattern pattern(String img) {
		Pattern p = new Pattern(img);
		return p;
	}

//	public float jFloat(float num){
//		return num;
//	}
//	
//	public double jDouble(double num){
//		return num;
//	}
//	
	public static void main(String[] args) {
		SikuliApi app =new SikuliApi();
		server = new GatewayServer(app);
	    server.start();
	}
}
