import { defineConfig, devices } from '@playwright/test';
import generateCustomLayoutSimpleExample from "./my_custom_layout";
import { LogLevel } from '@slack/web-api';
import * as dotenv from 'dotenv';

dotenv.config();

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 0 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI ? 
  [
    ["line"],
    ["html", { open: "never" }],
    ["junit", { outputFile: "junit.xml" }],
    ['playwright-json-summary-reporter'],
  ] : 
  [
    ["html", { open: "never" }],
    ['playwright-json-summary-reporter'],
  ],
  use: {
    trace: 'on-first-retry',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },

    // {
    //   name: 'firefox',
    //   use: { ...devices['Desktop Firefox'] },
    // },

    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
});
