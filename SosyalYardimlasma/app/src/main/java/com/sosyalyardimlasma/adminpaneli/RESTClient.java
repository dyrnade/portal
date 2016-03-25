package com.sosyalyardimlasma.adminpaneli;

import android.os.AsyncTask;
import android.util.Base64;
import android.util.Log;

import org.json.JSONException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.net.URLConnection;

/**
 * Created by bdurkut on 24/03/16.
 */

public class RESTClient {
    public static final String apiurl = "http://46.101.99.254/comodo/api_posts/";
    private static final String username = "gurescicem@gmail.com";
    private static final String password = "dyrnades*1";

    public static class DELETEOperation extends AsyncTask<String, Void, Integer> {
        @Override
        protected Integer doInBackground(String... params) {

            StringBuilder content = new StringBuilder();

            // many of these calls can throw exceptions, so i've just
            // wrapped them all in one try/catch statement.
            InputStream in = null;
            StringBuilder sb = new StringBuilder();
            int resCode = -1;

            try {

                URL url = new URL(apiurl+params[0]+"/");
                URLConnection urlConn = url.openConnection();

                if (!(urlConn instanceof HttpURLConnection)) {
                    throw new IOException("URL is not an Http URL");
                }
                HttpURLConnection httpConn = (HttpURLConnection) urlConn;
                String encoded = Base64.encodeToString((username + ":" + password).getBytes("UTF-8"), Base64.NO_WRAP);
                httpConn.setRequestProperty("Authorization", "Basic " + encoded);
                httpConn.setAllowUserInteraction(false);
                httpConn.setInstanceFollowRedirects(true);
                httpConn.setRequestMethod("DELETE");
                httpConn.connect();
                resCode = httpConn.getResponseCode();
                Log.d("DELETEOP", String.valueOf(resCode));

                /*if (resCode == HttpURLConnection.HTTP_OK) {
                    Log.d("DELETEOP", "Basarılı");
                }else{
                    Log.d("DELETEOP", "Hata olustu");
                }*/
            }

            catch (MalformedURLException e) {
                e.printStackTrace();
            }

            catch (IOException e) {
                e.printStackTrace();
            }

            return resCode;
        }

        @Override
        protected void onPostExecute(Integer s) {
            if(s < 300 && s >= 200)
                new RefreshList().execute();
            else{
                Log.d("REFRESHLIST", "Bir hata oluştu");
            }

        }
    }

    public static class PUTOperation extends AsyncTask<String, Void, Integer> {
        @Override
        protected Integer doInBackground(String... params) {

            int res = -1;

            try {
                URL url = new URL(apiurl+params[1]+"/");
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                String encoded = Base64.encodeToString((username + ":" + password).getBytes("UTF-8"), Base64.NO_WRAP);
                connection.setRequestProperty("Authorization", "Basic " + encoded);
                connection.setRequestMethod("PUT");
                connection.setDoOutput(true);
                connection.setRequestProperty("Content-Type", "application/json");
                connection.setRequestProperty("Accept", "application/json");
                OutputStreamWriter osw = new OutputStreamWriter(connection.getOutputStream());
                osw.write(params[0]);
                osw.flush();
                osw.close();
                res = connection.getResponseCode();
                Log.d("PUTDENEME", String.valueOf(connection.getResponseCode()));
            }catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (ProtocolException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            return res;
        }

        @Override
        protected void onPostExecute(Integer s) {
            if(s < 300 && s >= 200)
                new RefreshList().execute();
            else{
                Log.d("REFRESHLIST", "Bir hata oluştu");
            }

        }
    }

    public static class RefreshList extends AsyncTask<String, Void, String> {


        protected String doInBackground(String... urls) {

            return getUrlContents();
        }

        protected void onPostExecute(String output) {
            // TODO: check this.exception
            // TODO: do something with the feed
            try {
                if(output != null)
                    JsonParser.instantiate.refreshList(output);
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }
        public String getUrlContents()
        {
            StringBuilder content = new StringBuilder();

            // many of these calls can throw exceptions, so i've just
            // wrapped them all in one try/catch statement.
            InputStream in = null;
            StringBuilder sb = new StringBuilder();
            int resCode = -1;

            try {

                URL url = new URL(apiurl);
                URLConnection urlConn = url.openConnection();

                if (!(urlConn instanceof HttpURLConnection)) {
                    throw new IOException("URL is not an Http URL");
                }
                HttpURLConnection httpConn = (HttpURLConnection) urlConn;
                httpConn.setAllowUserInteraction(false);
                httpConn.setInstanceFollowRedirects(true);
                httpConn.setRequestMethod("GET");
                httpConn.connect();
                resCode = httpConn.getResponseCode();

                if (resCode == HttpURLConnection.HTTP_OK) {
                    in = httpConn.getInputStream();
                }else{
                    Log.d("REFRESHLIST", "sunucuya baglanamadı");
                }
            }

            catch (MalformedURLException e) {
                e.printStackTrace();
            }

            catch (IOException e) {
                e.printStackTrace();
            }
            if(resCode == HttpURLConnection.HTTP_OK) {
                String output = convertStreamToString(in);
                return output;
            }
            return null;
        }
    }

    private static String convertStreamToString(InputStream is) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        StringBuilder sb = new StringBuilder();

        String line = null;
        try {
            while ((line = reader.readLine()) != null) {
                sb.append(line).append('\n');
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                is.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return sb.toString();
    }



}
