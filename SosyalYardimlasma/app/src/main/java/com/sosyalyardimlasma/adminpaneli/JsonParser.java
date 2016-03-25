package com.sosyalyardimlasma.adminpaneli;

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by bdurkut on 24/03/16.
 */
public class JsonParser {
    private static final String TAG_ID = "id";
    private static final String TAG_USER = "user";
    private static final String TAG_TITLE = "title";
    private static final String TAG_MESSAGE = "message";
    private static final String TAG_ACC = "is_accomplished";


    public static JsonParser instantiate;
    RVAdapter adapter;

    public JsonParser(RVAdapter adapter) {
        this.adapter = adapter;
        instantiate = this;
    }

    public String publishPostString(PostManager.Post post) {
        JSONObject jpost = new JSONObject();
        try {
            jpost.put(TAG_TITLE, post.getTitle());
            jpost.put(TAG_MESSAGE, post.getMsg());
            jpost.put(TAG_ACC, true);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        return jpost.toString();
    }

    public void refreshList(String output) throws JSONException {
        Log.d("DENEME", output);
        PostManager.clearPosts();
        JSONArray posts = new JSONArray(output);
        //JSONObject jsonObj


        // Getting JSON Array node
        try {
            //posts = jsonObj.getJSONArray(TAG_POSTS);

            // looping through All Contacts
            for (int i = 0; i < posts.length(); i++) {
                JSONObject c = posts.getJSONObject(i);

                if (c.getBoolean(TAG_ACC) == false) {
                    int id = c.getInt(TAG_ID);
                    String title = c.getString(TAG_TITLE);
                    String message = c.getString(TAG_MESSAGE);

                    PostManager.Post post = new PostManager.Post(id, title, message);
                    PostManager.add_post(post);
                }

            }
            adapter.notifyDataSetChanged();

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}