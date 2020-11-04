import React from "react";
import logo from "./logo.svg";
import "./App.css";
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import BrawlerDetailPage from "./pages/brawler_detail";
import {BrawlerListPage} from "./pages/brawler_list";

function App() {
  return (
    <div className="App">
      <Router>
      <Switch>
          <Route path="/brawler/:brawlerId">
            <BrawlerDetailPage />
          </Route>
          <Route path="/">
            <BrawlerListPage />
          </Route>
        </Switch>
      </Router>
      
    </div>
  );
}

export default App;
