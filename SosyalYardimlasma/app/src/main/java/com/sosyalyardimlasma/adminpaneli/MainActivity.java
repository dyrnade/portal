package com.sosyalyardimlasma.adminpaneli;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.Menu;
import android.view.MenuItem;

import com.sosyalyardimlasma.adminpaneli.R;


public class MainActivity extends Activity {

    private static Context context;

    RESTClient rc;
    public RVAdapter adapter;
    JsonParser jp;

    public static Context getAppContext() {
        return MainActivity.context;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        MainActivity.context = getApplicationContext();

        final RecyclerView rv = (RecyclerView)findViewById(R.id.rv);
        LinearLayoutManager llm = new LinearLayoutManager(this);
        rv.setLayoutManager(llm);

        adapter = new RVAdapter(PostManager.POSTS, MainActivity.this);
        rv.setAdapter(adapter);

        jp = new JsonParser(adapter);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);
        getMenuInflater().inflate(R.menu.actionmenu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.action_refresh:
                new RESTClient.RefreshList().execute();
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

}
